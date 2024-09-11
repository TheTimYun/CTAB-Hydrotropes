# Please read before use  
**TLDR**: to get information if the system is viscous, please use 'calculator.py' script. You should have RDKIt, MolFeat and XGBBoost packages installed, along with Pandas and Numpy.  
You should type down CTAB concentraion, additive concentrion, temperature and SMILES of the additive. If additive is ionized, depending on the pH, assng correct charges. You will get classes of solutions: 1 - gel (>10 cP), 0 - no gel (<10 cP). You will also get viscosity values in cP. However, viscosity values will not always match data, obtained with classification and should be trusted with caution.  

This set of files was made as an attempt to correctly classify hydrotropes-contaning systems with CTAB (cetrimonium bromide) with simples ML methods (**no neural ntworks**... so far). As any ML task is divided on multiple steps, I created several files to guide anyone who is interested stepwise. Files are:  
1. *Data.xslx* - raw data, collected from articles, with all necessary references. Contains SMILES of the additive, temperature, concentraion of SMILES and addtive, ratio of CTAB and additive, class: 0  if viscosity is greater less 10 cP, otherwise 1, viscosity, reference. If pH is changed, ionization is added to the SMILES of the additive.  
2. *Hydrotropes.ipynb* - here Dataset is processed and transormed into two sets of descriptors:
    -Full feature sets: *X_standard.pickle* and *X_padel.pickle* - full sets )
    -Feature sets where correlated features are dropped (*X_standard_dropped.pickle*, *X_padel_dropped.pickle*)
    -Target sets (*y.pickle* - classes, *viscosity.pickle* - viscosity), 
