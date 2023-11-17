# Heart Disease Prediction App Project

## Model Testing

Instructions: If running the Model Testing .ipynb notebooks, be sure to replace the CSV file path for the  "data2" variable below:

- data2 = pd.read_csv('static_[null]/heart_integer_v01.csv')

  ...with the new, replacement file path:

- data2 = pd.read_csv('../data/cleaned data/heart_integer_v01.csv')

- `Models Tested`:

  - Decision Trees
  - Logistic Regression
  - RandomForest Classifier
  - XGBoost

- `Dataframes Tested` in each Model:
  - One-Hot Encoded Integer Dataset
  - MinMax Scaler Dataset
  - Standard Scaler Dataset
