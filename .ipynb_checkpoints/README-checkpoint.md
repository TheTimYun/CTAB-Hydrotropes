# Please read before use  
**TLDR**: to get information if the system is viscous, please use 'calculator.py' script. You should have RDKIt, MolFeat and XGBBoost packages installed, along with Pandas and Numpy. You should type down CTAB concentraion, additive concentrion, temperature and SMILES of the additive. If additive is ionized, depending on the pH, assng correct charges. You will get classes of solutions: 1 - gel (>10 cP), 0 - no gel (<10 cP). You will also get viscosity values in cP. However, viscosity values will not always match data, obtained with classification and should be trusted with caution.  

This set of files was made as an attempt to correctly classify hydrotropes-contaning systems with CTAB (cetrimonium bromide).
