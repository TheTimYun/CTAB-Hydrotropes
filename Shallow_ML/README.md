This folder contains following files:


1. **"Data.xslx"** - raw data, collected from different articles, **without any references**. Contains SMILES of the additive, temperature, concentraion of SMILES and addtive, ratio of CTAB and additive, class: 0  if viscosity is greater less 10 cP, otherwise 1, viscosity, reference. If pH is changed, ionization is added to the SMILES of the additive.  

2. **"1.Data processing.ipynb"** - here Dataset is processed and transormed into sets of descriptors:
    - Full feature sets: *X_standard.pickle* and *X_padel.pickle* (Pandas)
    - Feature sets where most correlated features are dropped: *X_standard_dropped.pickle*, *X_padel_dropped.pickle*) (Pandas);
    - Feature sets with reduced number of features with PCA: *X_standard_pca.pickle*, *X_padel_pca.pickle*) (Pandas);
    - Features to drop - *features_to_drop_Standard.pickle*, *features_to_drop_Padel.pickle* - indices of features to drop (NumPy);
    - Target sets: *y.pickle* - classes, *viscosity.pickle* - viscosity (Pandas);
    - Imputer: SkLeaent imputer to fill in mising values in table of descriptors;
    - Groups set, which contains information unique SMILES for grouping for species-specific cross-validations - *groups.pickle* (Pandas).

3. **"2.ML_standard_hp.ipynb"** - here the algorithm of ML method selection is described. First, the function to make automatic calculation and its helping functions are presented. Then, performance of several algorithms is evaluated with 5-fold cross-validation on training set:
   - Logistic Regression
   - Random Forest
   - Gradient Bossting (as implemented in XGBoost)
   - Support Vector Machine
   - KNearestNeighbors
  The performance is assesed with f1-score, accuracy, roc-auc acore and ROC-AUC curve. Hyperparameters of each algorithm are optimized with hyperopt package. It was found, that XGBoost on standard RDKIt descriptors is the best one. The performance table is dumped with *score_hyper_opt.pickle*

4. **"3.ML_with_groups.ipynb"** is analogous to the previous one, except for the one feature: splitting on the training and test set is performed in a way that all samples with the same compound as an additive would be in the same set during cross-validation. It was found, that cross-validation performance in that case is generally lower and Random Forest shows the best metrics . The performance table is dumped with *score_groups_hyper_opt.pickle*

5. **"4.Regression model for viscosity:** - here the best parameters for the viscosity regression (using XGBRegressor) on the base of descriptors are found. 

6. **"5.Final_classification_model.ipynb"** - here we create trained models with parameters, which were found earlier. Also, we assess the relative importance of descriptors for the classification and regression tasks. Also, here results may be obtained  with SMILES of the additive, CTAB and additive concentration and temperature. *trained_model_clf.pickle* and *trained_model_reg.pickle* are the files with trained models for classification and regression, respectively.

7. **calculator.py** is the light version, that get the results for your system in a terminal. All you need is hust to have several packages installed (described in the first paragraph here) and enter parameters of the system.This 