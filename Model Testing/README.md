# Heart Disease Prediction App Project

## Model Testing

## Purpose
These notebooks aim to Test 3 types of encoded DataSets (One-Hot Encoded Integer Dataset, MinMax Scaler Dataset, Standard Scaler Dataset) across 4 Models  (Decision Trees, Logistic Regression, RandomForest Classifier, XGBoost). Primary goal was to find Highest Accuracy Score and Lowest False Negatives.

## Tools Used

The optimization process utilized the following key tools and libraries:
- `pandas`: For data manipulation and analysis.
- `sklearn.metrics`: To compute various performance metrics like accuracy, precision, recall, F1 score, ROC-AUC, and R2 score.
- `numpy`: For numerical computing.
- `matplotlib.pyplot`: For creating plots to visualize results.
- `from sklearn.tree import DecisionTreeClassifier`: Decision Tree
- `from sklearn.linear_model import LogisticRegression`: Logistic Regression
- `from sklearn.ensemble import RandomForestClassifier`: RandomForest Classifier
- `import xgboost as xgb`: XGBoost


## Model Performance - Accuracy

| Accuracy Score - One-Hot Integer Dataset | Accuracy Score - StandardScaler Scaled Dataset | Accuracy Score - MinMax Scaled Dataset |
|------------------------------------------|-----------------------------------------------|----------------------------------------|
| 1 - Random Forest Classifier - 88.5 %    | 1 - Random Forest Classifier - 88.5 %         | 1 - Random Forest Classifier - 88.5 %  |
| 2 - XGBoost - 88.0 %                     | 2 - XGBoost - 88.0 %                          | 2 - XGBoost - 88.0 %                   |
| 3 - Deep Learning-Adam Optimizer - 86.5 %| 3 - Deep Learning-Adam Optimizer - 86.5 %     | 3 - Logistic Regression - 86.4 %      |
| 4 - Logistic Regression - 85.3 %         | 4 - Logistic Regression - 85.3 %              | 4 - Deep Learning-Adam Optimizer - 85.6 % |
| 5 - Decision Tree Classifier - 79.8 %    | 5 - Decision Tree Classifier - 78.2 %         | 5 - Decision Tree Classifier - 78.8 % |



## Model Performance - Confusion Matrix (One-Hot Integer DataSet)


| True Positives                  | True Negatives                  | False Positives                | False Negatives                |
|----------------------------------|----------------------------------|----------------------------------|----------------------------------|
| 1 - Random Forest Classifier: 94 | 1 - XGBoost: 70                 | 1 - Decision Tree Classifier: 12 | 1 - Decision Tree Classifier: 25 |
| 2 - XGBoost: 92                   | 2 - Random Forest Classifier: 69 | 2 - Logistic Regression: 10     | 2 - Logistic Regression: 17     |
| 3 - Logistic Regression: 90       | 3 - Logistic Regression: 67     | 3 - Random Forest Classifier: 8 | 3 - XGBoost: 15                 |
| 4 - Decision Tree Classifier: 82 | 4 - Decision Tree Classifier: 65 | 4 - XGBoost: 7                  | 4 - Random Forest Classifier: 13|



## Models & DataFrames

`Models Tested`:
  - Decision Trees
  - Logistic Regression
  - RandomForest Classifier
  - XGBoost

`Dataframes Tested` in each Model:
  - One-Hot Encoded Integer Dataset
  - MinMax Scaler Dataset
  - Standard Scaler Dataset


## Instructions

If running any of the Model Testing `.ipynb` notebooks, be sure to replace the CSV file path for the  `data2` variable below:

- `data2 = pd.read_csv('static_[null]/heart_integer_v01.csv')`

  ...with the new, replacement file path:

- `data2 = pd.read_csv('../data/cleaned data/heart_integer_v01.csv')`



