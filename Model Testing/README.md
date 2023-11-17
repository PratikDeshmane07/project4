# Heart Disease Prediction App Project

## Model Testing

## Purpose
These notebooks aim to Test 3 types of encoded DataSets (One-Hot Encoded Integer Dataset, MinMax Scaler Dataset, Standard Scaler Dataset) across 4 Models  (Decision Trees, Logistic Regression, RandomForest Classifier, XGBoost)

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

Accuracy Score - One-Hot Integer Dataset
- 1 - Random Forest Classifier - 88.5 %
- 2 - XGBoost - 88.0 %
- 3 - Deep Learning-Adam Optimizer - 86.5 %
- 4 - Logistic Regression - 85.3 %
- 5 - Decision Tree Classifier - 79.8 %

Accuracy Score - StandardScaler Scaled Dataset
- 1 - Random Forest Classifier - 88.5 %
- 2 - XGBoost - 88.0 %
- 3 - Deep Learning-Adam Optimizer - 86.5 %
- 4 - Logistic Regression - 85.3 %
- 5 - Decision Tree Classifier - 78.2 %

Accuracy Score - MinMax Scaled Dataset
- 1 - Random Forest Classifier - 88.5 %
- 2 - XGBoost - 88.0 %
- 3 - Logistic Regression - 86.4 %
- 4 - Deep Learning-Adam Optimizer - 85.6 %
- 5 - Decision Tree Classifier - 78.8 %


## Models & DataFrames

`Models Tested`:
  - Decision Trees
  - Logistic Regression
  - RandomForest Classifier
  - XGBoost

- `Dataframes Tested` in each Model:
  - One-Hot Encoded Integer Dataset
  - MinMax Scaler Dataset
  - Standard Scaler Dataset


## Instructions

If running the Model Testing .ipynb notebooks, be sure to replace the CSV file path for the  "data2" variable below:

- data2 = pd.read_csv('static_[null]/heart_integer_v01.csv')

  ...with the new, replacement file path:

- data2 = pd.read_csv('../data/cleaned data/heart_integer_v01.csv')



