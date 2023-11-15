# Model Optimization - RandomForest_ModelOptimization_#2

## Overview
The `RandomForest_ModelOptimization_#2.ipynb` notebook is dedicated to the optimization of a Random Forest classifier used in our data analysis project.

## Purpose
This notebook aims to fine-tune the Random Forest model to enhance its predictive performance on our dataset. It iteratively adjusts model hyperparameters to identify the most effective model settings.

## Tools Used
The optimization process utilized the following key tools and libraries:
- `pandas`: For data manipulation and analysis.
- `sklearn.ensemble`: To import the RandomForestClassifier.
- `sklearn.model_selection`: For splitting the dataset and utilizing GridSearchCV.
- `sklearn.metrics`: To compute various performance metrics like accuracy, precision, recall, F1 score, ROC-AUC, and R2 score.
- `numpy`: For numerical computing.
- `matplotlib.pyplot`: For creating plots to visualize results.

The most crucial tool was `GridSearchCV` from `sklearn.model_selection`, which was instrumental in searching for the ideal set of hyperparameters for our Random Forest model.

## Final Model Performance
The optimized Random Forest model achieved the following performance metrics:
- **Accuracy**: 0.8804
- **Precision**: 0.8972
- **Recall**: 0.8972
- **F1 Score**: 0.8972
- **AUC-ROC**: 0.8772
- **R2 Score**: 0.5837

These metrics indicate a robust model with high classification accuracy and predictive power.

## Optimized Parameters
The final optimized hyperparameters for the model are:
- **bootstrap**: True
- **max_depth**: 20
- **min_samples_leaf**: 1
- **min_samples_split**: 2
- **n_estimators**: 290

These parameters were determined to yield the best balance between bias and variance, leading to a model that generalizes well on unseen data.

## Contributors
- **Eric**: Carried out the optimization process, fine-tuning the hyperparameters, and evaluating the model performance.
