import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
import numpy as np  

# Load the trained model
model = joblib.load('random_forest_11_features.joblib')

# Feature names as they appear in the model
feature_names = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 
                 'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope']

# Function to get feature importance
def get_feature_importance(model, feature_names):
    importances = model.feature_importances_
    sorted_indices = np.argsort(importances)[::-1]
    return [(feature_names[i], importances[i]) for i in sorted_indices]

# Get and display feature importance
feature_importance = get_feature_importance(model, feature_names)
print(feature_importance)
