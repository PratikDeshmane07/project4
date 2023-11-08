import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
df = pd.read_csv('heart.csv')

# Assuming 'Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope' are categorical
categorical_features = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']

# Convert categorical variables using LabelEncoder
label_encoders = {}
for column in categorical_features:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])

# Assuming 'Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak' are numerical
# and 'FastingBS' should be converted to integer if it's not already
df['FastingBS'] = df['FastingBS'].astype(int)

# Split the data into features and target
X = df.drop('HeartDisease', axis=1)  # Assuming 'HeartDisease' is the target variable
y = df['HeartDisease']

# Split the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'random_forest_11_features.joblib')

# Check the number of features
print(model.n_features_in_)  # Should output 11
