Ths folder contains files and notebooks, which are dedicated to implement fully connected Neural Networks (GNN) to predict geleous state of CTAB-organic additive solution. To implement fully connected NN you need all the packages, that were used for shallow ML, [PyTorch](https://pytorch.org/), and, if you want to try looking for optimal architecture search by youself - [wandb][https://wandb.ai/site/]. However, the performance of this type of NN is not very high with accuracy only of 0.67.  
This folder contains following files:  
1. **1.Architecture_selection.ipynb** - describes the process of search for optimal architecture of NN;
2. **X_standard_dropped.pickle**, **X_padel_dropped.pickle**, **y.pickle**, **groups.pickle**, **features_to_drop.pickle** - files from the shallow ML workflow first file, **Data_processing.ipynb**, that contains descriptors table, targets, groups of chemical additives, features of to drop from the NN input. 
3. **Search_for_optimal_parameters-Accuracy.ipynb** - describes the process of search for optimal hyperpearameters, training and assessment of NN;
4. **scaler.pickle** - sklearn scaler for final caclulator;
5. **model_standard_dict_state.pth** - dict state for final model;
6. **best_params_padel.pickle** and **best_params_standard.pickle** - best hyperparameters for NN for Standard and PaDEL descriptors;
8. **calculator.py** -  calculator to predict the final state of system.

The basic NN class is:

    'class Classification_NN(nn.Module):
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
        '

Best parameters for standard descriptors are n_descriptors = 1871, n1 = 4576, n2 = 932, n3, epochs = 300. 