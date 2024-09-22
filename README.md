# Please read before use  
**TLDR**: to get information if the system is viscous, please use 'calculator.py' script. You should have RDKIt, MolFeat and XGBBoost packages installed, along with Pandas and Numpy.  
You should type down CTAB concentraion, additive concentrion, temperature and SMILES of the additive. If additive is ionized, depending on the pH, assng correct charges. You will get classes of solutions: 1 - gel (>10 cP), 0 - no gel (<10 cP). You will also get viscosity values in cP. However, viscosity values will not always match data, obtained with classification and should be trusted with caution.  

This set of files was made as an attempt to correctly classify hydrotropes-contaning systems with CTAB (cetrimonium bromide) with simples ML methods (**no neural networks**... so far). As any ML task is divided on multiple steps, I created several files to guide anyone who is interested stepwise. Files are:  
1. *Data.xslx* - raw data, collected from articles, with all necessary references. Contains SMILES of the additive, temperature, concentraion of SMILES and addtive, ratio of CTAB and additive, class: 0  if viscosity is greater less 10 cP, otherwise 1, viscosity, reference. If pH is changed, ionization is added to the SMILES of the additive.  
2. *1. Hydrotropes.ipynb* - here Dataset is processed and transormed into sets of descriptors:
    - Full feature sets: *X_standard.pickle* and *X_padel.pickle* 
    - Feature sets where most correlated features are dropped: *X_standard_dropped.pickle*, *X_padel_dropped.pickle*)
    - Features to drop - *features_to_drop.pickle*
    - Target sets: *y.pickle* - classes, *viscosity.pickle* - viscosity
    - Groups set, which contains information unique SMILES about grouping for species-specific cross-validations - *groups.pickle*

3. *2.ML_standard_hp.ipynb* - here the main calculation proceeds. First, the function to make automatic calculation and its helping functions are presented. Then, performance of several algorithms is evaluated with 5-fold cross-validation on training set:
   - Logistic Regression
   - Random Forest
   - Gradient Bossting (as implemented in XGBoost)
   - Support Vector Machine
   - KNearestNeighbors
  The performance is assesed with f1-score, accuracy, roc-auc acore and ROC-AUC curve. Hyperparameters of each algorithm are optimized with hyperopt package. It was found, that XGBoost on standard RDKIt descriptors is the best one. The performance table is dumped with *score_hyper_opt.pickle*

4. *3 ML_with_groups.ipynb* is analogous to the previous obne, except one feature: splitting on the training and test set is performed such that all samples with the same compound as an additive would be in the same set during cross-validation. It was found, that cross-validation performance in that case is generally lower and Random Forest is the best algorithm in this case. The performance table is dumped with *score_groups_hyper_opt.pickle*
