import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('random_forest_11_features.joblib')

def main():
    # Setting page configuration with a heart icon and a title with a health emoji
    st.set_page_config(page_title="❤️ Heart Disease Prediction App", page_icon="❤️", layout="wide")

    st.title("💉 Heart Disease Prediction App")

    # Input features from the user
    age = st.number_input('Age', min_value=0, max_value=120, value=30)  # Assuming age is from 0 to 120
    sex = st.selectbox('Sex', ['Male', 'Female'])
    chest_pain_type = st.selectbox('Chest Pain Type', ['TA', 'ATA', 'NAP', 'ASY'])
    resting_bp = st.number_input('Resting Blood Pressure', value=120)
    cholesterol = st.number_input('Cholesterol', value=200)
    fasting_bs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['No', 'Yes'])
    resting_ecg = st.selectbox('Resting Electrocardiogram Results', ['Normal', 'ST', 'LVH'])
    max_hr = st.number_input('Maximum Heart Rate Achieved', value=120)
    exercise_angina = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
    oldpeak = st.number_input('ST depression induced by exercise relative to rest', value=1.0)
    st_slope = st.selectbox('The slope of the peak exercise ST segment', ['Up', 'Flat', 'Down'])

    # When 'Predict' is clicked, make the prediction and store it under the variable 'prediction'
    if st.button('Predict'):
        # Encode the inputs
        sex_encoded = 0 if sex == 'Male' else 1
        chest_pain_type_encoded = ['TA', 'ATA', 'NAP', 'ASY'].index(chest_pain_type)
        fasting_bs_encoded = 0 if fasting_bs == 'No' else 1
        resting_ecg_encoded = ['Normal', 'ST', 'LVH'].index(resting_ecg)
        exercise_angina_encoded = 0 if exercise_angina == 'No' else 1
        st_slope_encoded = ['Up', 'Flat', 'Down'].index(st_slope)

        input_data = np.array([age, sex_encoded, chest_pain_type_encoded, resting_bp, cholesterol, fasting_bs_encoded, resting_ecg_encoded, max_hr, exercise_angina_encoded, oldpeak, st_slope_encoded]).reshape(1, -1)
        prediction = model.predict(input_data)
        st.write('## Prediction Result:')
        if prediction[0] == 1:
            st.error('The model predicts a risk of heart disease.')
        else:
            st.success('The model predicts no heart disease.')

if __name__ == '__main__':
    main()
