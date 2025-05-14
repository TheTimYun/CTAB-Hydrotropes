import pickle
from rdkit.Chem import AllChem
from rdkit import Chem
import pandas as pd
import numpy as np
from molfeat.calc import RDKitDescriptors2D, RDKitDescriptors3D
from molfeat.trans import MoleculeTransformer
import datamol as dm
import torch
import torch.nn as nn

#Function definition
def embed_optimize(smi):
    ''' This function makes 3D optimized instance of  RDKit Molecule only from its smiles
    '''
    m = Chem.MolFromSmiles(smi)
    m = Chem.AddHs(m)
    AllChem.EmbedMolecule(m)
    AllChem.MMFFOptimizeMolecule(m, maxIters=500)
    return m


class Classification_NN(nn.Module):
    def __init__(self, n_descriptors, n1, n2, n3):
        super().__init__()
        self.linear_1 = nn.Linear(n_descriptors, n1)
        self.a1 = nn.Mish()
        self.dropout_1 = nn.Dropout(p = 0.3)
        self.linear_2 = nn.Linear(n1, n2)
        self.a2 = nn.Mish()

        self.linear_3 = nn.Linear(n2, n3)
        self.a3 = nn.Mish()
        
        self.linear_4 = nn.Linear(n3, 2)
    def forward(self, x):
        x = self.a1(self.linear_1(x))
        x = self.dropout_1(x)
        x = self.a2(self.linear_2(x))
        x = self.a3(self.linear_3(x))
        x = self.linear_4(x)
        return x
        
#Model loading
with open('best_params_standard.pickle', 'rb') as inp:
    best_params = pickle.load(inp)


with open('features_to_drop_Standard.pickle', 'rb') as inp:
    features_to_drop = pickle.load(inp)



with open('scaler.pickle', 'rb') as inp:
    scaler = pickle.load(inp) 


#Initializing the model
model_clf = Classification_NN(n_descriptors = 1871, n1 = best_params['n1'], n2 = best_params['n2'], n3 = best_params['n3'])

#Loading state_dict for the best model
model_clf.load_state_dict(torch.load('model_standard_dict_state.pth'))
model_clf.eval()

#AllNecessaryInputs
CTAB_conc = int(input('Enter CTAB concentration here'))

additive_conentrations = input('Enter additive concentraions in mM like 50,80,60,90 ')
additive_conentrations = [int(x) for x in additive_conentrations.split(',')]
temp = int(input('Enter the temperature in Celcius degrees '))
SMILES = input('Enter the SMILES of the additive ')
add = embed_optimize(SMILES)

#Creating descriptors
fp = AllChem.GetMorganFingerprintAsBitVect(add, radius = 3)
fp_df = pd.DataFrame(np.array(fp).reshape(1,-1), columns = ['fp{}'.format(i) for i in range(2048)])
#descriptors calculation
calc_2D = RDKitDescriptors2D()
calc_3D = RDKitDescriptors3D()
with dm.without_rdkit_log():
    feats_2D = calc_2D(add)
    feats_3D = calc_3D(add)

features = pd.DataFrame(np.concatenate([feats_2D, feats_3D]).reshape(1,-1), columns=calc_2D.columns + calc_3D.columns)
features = pd.concat([fp_df, features], axis = 1)



dic = {'CTAB concentration (mM)':[], 'Additive concentration':[], 'CTAB/additive':[], 'Temperature':[] }
for conc in additive_conentrations:
    dic['CTAB concentration (mM)'].append(CTAB_conc)
    dic['Additive concentration'].append(conc)
    dic['CTAB/additive'].append(CTAB_conc/conc)
    dic['Temperature'].append(temp)
df = pd.DataFrame(dic)
X = pd.concat([df, pd.concat([features]*len(additive_conentrations), ignore_index= True)], axis = 1)
X.drop(columns=['Alerts'], inplace=True)
X = X.drop(columns = features_to_drop)
X = scaler.transform(X)
X = torch.tensor(X, dtype = torch.float32)
model_clf.to('cuda:0')
X = X.to('cuda:0')


probs = torch.softmax(model_clf(X), dim = 1)
classes = torch.argmax(probs, dim = 1)

print(probs)
print(classes)
    