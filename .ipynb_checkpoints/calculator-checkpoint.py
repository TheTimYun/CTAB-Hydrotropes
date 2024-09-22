import pickle
from rdkit.Chem import AllChem
from rdkit import Chem
import pandas as pd
import numpy as np
from molfeat.calc import RDKitDescriptors2D, RDKitDescriptors3D
from molfeat.trans import MoleculeTransformer
import datamol as dm
from xgboost import XGBClassifier, XGBRegressor


#Function definition
def embed_optimize(smi):
    ''' This function makes 3D optimized instance of  RDKit Molecule only from its smiles
    '''
    m = Chem.MolFromSmiles(smi)
    m = Chem.AddHs(m)
    AllChem.EmbedMolecule(m)
    AllChem.MMFFOptimizeMolecule(m, maxIters=500)
    return m

#Model loading
with open('trained_model_clf.pickle', 'rb') as inp:
    trained_model_clf = pickle.load(inp)

with open('trained_model_reg.pickle', 'rb') as inp:
    trained_model_reg = pickle.load(inp)

with open('features_to_drop.pickle', 'rb') as inp:
    features_to_drop = pickle.load(inp)

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

classes = trained_model_clf.predict(X)
viscosity = 1000*np.exp(trained_model_reg.predict(X))

print(classes)
print(viscosity)
    