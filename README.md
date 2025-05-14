# Please read before use  
**TLDR**: to get information if the quesous system of CTAB and chemical additive is viscous, please use 'calculator.py' script. You should have RDKit, MolFeat, DataMol and XGBBoost packages installed, along with Pandas and Numpy to use shallow ML methods, PyTorch, PyTorch_geometric, ChemLib, Torchmetrics to use NNs
You will be prompt to type down CTAB concentraion, additive concentrations, temperature and SMILES of the additive. If additive is ionized, depending on the pH, assign correct charges to atoms in SMILES notation. You will get classes of solutions: 1 - gel (>10 cP), 0 - no gel (<10 cP). You will also get viscosity values in cP. However, viscosity values will not always match data, obtained with classification and should be trusted with caution.  

This set of files was made as an attempt to correctly classify hydrotropes-contaning systems with CTAB (cetrimonium bromide) with simple ML methods and (**UPDATE**) Fully-connected and Graph Neural networks. As any ML task is divided on multiple steps, I created several files to guide anyone who is interested stepwise.  

Here you can find several folders and one file:

1. **Shallow_ML** - contains notebooks, that deal with descriptors calculation and implementing shallow ML methods;
2. **NNs** - contain notebooks, that implement NNs to predict the geleous state of CTAB-containing systems;
3. **Data_with_reference.xlsx** is the initial dataset with all necessary references.  

Instructions and descriptions for all notebooks are located in respective folders.

---
If you have any problems, questions or suggestions, please don't hesitate to contact me at timyun96@gmail.com



