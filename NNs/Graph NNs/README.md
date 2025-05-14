Ths folder contains files and notebooksm which are dedicated to implement Graph Neural Networks (GNN), using PyTorch geometric to predict geleous state of CTAB-organic additive solution. To implement GNN, you need [PyTorch geometric](https://pytorch-geometric.readthedocs.io/en/latest/), [chemlib](https://chemlib.readthedocs.io/en/latest/. ) and [Torchmetrics](https://lightning.ai/docs/torchmetrics/stable/) besides libraries, described earlier for ML methods and Fully-connected NNs. However, you don't need to always bring all these scalers and imputers with you. The least possible amount of data - SMILES, conncentrations and temperatures. 

This folder contains following files:  
1. **1.Architecture_selection.ipynb** - describes the process of search for optimal architecture of GNN;
2. **Data.xslx** - dataset with concnetrations, chemical structure and taeget;
3. **groups.pickle** - for grouping of dataset instances according to chemical nature;
4. **Search_for_optimal_parameters-Accuracy.ipynb** - describes the process of search for optimal hyperpearameters, training and assessment of GNN;
5. **model_standatd_acc.pickle** - final model for calculations;
6. **best_params.pickle** - best hyperparameters for GNN
7. **Calculator.ipynb** - Jupyter Notebook calculator to predict the final state of system.

The basic GNN class is:

    'class Graph_nn(nn.Module):
        def __init__(self, num_node_features = 21, n1 = 500, n2 = 500):
            super().__init__()
            self.nn_conv_1 = NNConv(in_channels = num_node_features, out_channels = n1, nn = nn.Sequential(nn.Linear(4, n1), nn.CELU(), nn.Linear(n1, 21*n1)))
            self.a_nn_conv1 = nn.CELU()
            
            self.edge_conv_3 = EdgeConv(nn = nn.Sequential(nn.Linear(2*n1, n2), nn.CELU(), nn.Linear(n2,n2)))
            self.a3 = nn.CELU()
            
            self.edgepool = EdgePooling(in_channels = n2,  dropout = 0.3) 
            self.linear_1 = nn.Linear(in_features = n2, out_features = 2)
    
            
        def forward(self, data):
            x, edge_index, edge_attr  = data.x, data.edge_index, data.edge_attr
            x = self.a_nn_conv1(self.nn_conv_1(x = x, edge_index = edge_index, edge_attr = edge_attr))
            x = self.a3(self.edge_conv_3(x = x, edge_index = edge_index))
           
            if data.batch is None:
                batch = torch.zeros(x.size(0), dtype=torch.long, device=x.device)
            else:
                batch = data.batch
     
            x, new_edge_index, batch_assign, _ = self.edgepool(x = x, edge_index = edge_index, batch = batch)
            x = global_add_pool(x, batch = batch_assign)
            x = self.linear_1(x)
            return x
        '

Best parameters are n1 = 408, n2 = 29, epochs = 39.