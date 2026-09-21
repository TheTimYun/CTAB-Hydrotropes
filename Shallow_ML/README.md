Here we present the results of shallow methods application for the prediction of rheological state of CTAB solutions with the organic additives. Following libraries should be installed:

```

rdkit == 2024.03.5 scikit-learn==1.5.1 hyperopt==0.2.7 molfeat==0.10.1 molfeat-padel=0.0.2 padelpy==0.1.17 pandas==2.2.2 numpy==1.26.4 datamol==0.12.5

```



This folder contains following files:


1. **"Data.xslx"** - raw data, collected from different articles, **without  references**. Contains SMILES of the additive, temperature, concentraion of SMILES and addtive, ratio of CTAB and additive, rheological state (Is_gel column), viscosity, reference. Ionic form is accounted in SMILES of the additive  

2. **"1.Data processing.ipynb"** - here вataset is processed and transormed into descriptor sets:
    - Full feature sets: *X_standard.pickle* and *X_padel.pickle* (Pandas)
    - Target set: *y.pickle* - classes
    - Groups set, which contains information about SMILES for grouping for structure-based splitting strategy during cross-validation and evlauation on the test set - *groups.pickle* (Pandas).

3. **"2a.Classification_random_sp-lit.ipynb"** - here algorithm and optimal hyperparamters are selected. First, the function to make automatic calculation and its helping functions are presented. Then, performance of several algorithms is evaluated with cross-validation on training set:
   - Logistic Regression
   - Random Forest
   - Gradient Bossting (as implemented in XGBoost)
   - Support Vector Machine
   - KNearestNeighbors
  Hyperparamres optimization is performe during CV. Then, model is trained using optimal hyperparameters and its performance is assesed with precision, f1-score, accuracy, roc-auc acore and ROC-AUC curve. Curve is then saved to special folder (*ROC_AUC_all_temps_random*). Hyperparameters of each algorithm are optimized with hyperopt package. It was found that RF on standard RDKIt descriptors is the best-performing. The performance table is dumped with *score_clf_random_all_temp.pickle* )Pandas)

4. **"2c.Classification_structure_based_split.ipynb"** - performs the same actions, that the file above, but emppolying structure-based splitting strategy. Scores file is *score_clf_structure_all_temp.pickle*, ROC-AUC curves are saved to *ROC_AUC_all_temps_structure_based*


5. **"3.Final_classification_model.ipynb"** - here we create trained model with optimal parameters found earlier. Also, we assess the relative importance of descriptors. Prediction for unseen system can be made in this file  with SMILES of the additive, CTAB and additive concentration and temperature. *trained_model_clf.pickle* is the file with the instance of trained model.

6. **calculator.py** is the light version, that make predictions for your system All you need is to have several packages installed (described in the first paragraph ) and enter parameters. Calculator can be launched in terminal with

```
python calculator.py

```

**Base classifiers** folder contains files, that describe the development of models, trained on system properties only and molecular descriptors only. Results are used as supplement to reveal the role of both types of descriptors in final predictions. 