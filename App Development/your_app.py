import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('random_forest_11_features.joblib')

def main():
    # Setting page configuration with a heart icon and a title with a stethoscope and heart emoji
    st.set_page_config(page_title="❤️ Heart Disease Prediction App", page_icon="❤️", layout="wide")

    st.title("🩺❤️ Heart Disease Prediction App")

    # Input features from the user
    age = st.number_input('Age', min_value=0, max_value=120, value=30)
    sex = st.selectbox('Sex', ['Male', 'Female'])
    chest_pain_type = st.selectbox('Type of Chest Pain', ['TA', 'ATA', 'NAP', 'ASY'])
    resting_bp = st.number_input('Resting Blood Pressure (mm Hg)', value=120)
    cholesterol = st.number_input('Cholesterol Level (mg/dL)', value=200)
    fasting_bs = st.selectbox('Fasting Blood Sugar Level (> 120 mg/dL)', ['No', 'Yes'])
    resting_ecg = st.selectbox('Resting ECG Results', ['Normal', 'ST', 'LVH'])
    max_hr = st.number_input('Maximum Heart Rate Achieved', value=120)
    exercise_angina = st.selectbox('Exercise Induced Chest Pain', ['No', 'Yes'])
    oldpeak = st.number_input('Exercise-related ST Depression (mm)', value=1.0)
    st_slope = st.selectbox('ST Segment Response to Exercise', ['Up', 'Flat', 'Down'])

    # Feature advice, lifestyle suggestions, and potential medications
    feature_advice = {
        'Age': {
            'advice': "While age can't be changed, understanding risk factors is important.",
            'lifestyle': "Focus on a heart-healthy lifestyle regardless of age.",
            'medication': None
        },
        'Sex': {
            'advice': "Risk can vary with sex, but both genders should maintain a healthy lifestyle.",
            'lifestyle': "Regular check-ups and healthy living are important for all.",
            'medication': None
        },
        'Type of Chest Pain': {
            'advice': "Certain types like 'ASY' are more associated with heart risk.",
            'lifestyle': "Be aware of chest pain types and consult a doctor if it's unusual.",
            'medication': None
        },
        'Resting Blood Pressure': {
            'advice': "Aim for a normal range (120/80 mm Hg).",
            'lifestyle': "Regular exercise, a healthy diet, and weight management can help.",
            'medication': "Medications like ACE inhibitors may be prescribed for high BP."
        },
        'Cholesterol Level': {
            'advice': "High cholesterol increases risk. Aim for below 200 mg/dL.",
            'lifestyle': "A diet low in saturated fats and regular exercise can help.",
            'medication': "Statins may be prescribed for managing high cholesterol."
        },
        'Fasting Blood Sugar Level': {
            'advice': "Keep it below 120 mg/dL to reduce risk.",
            'lifestyle': "A balanced diet and regular exercise are key to controlling blood sugar.",
            'medication': "Medications like metformin can help in managing blood sugar levels."
        },
        'Resting ECG Results': {
            'advice': "Abnormal ECG results can indicate higher risk.",
            'lifestyle': "Regular monitoring and a heart-healthy lifestyle are important.",
            'medication': None
        },
        'Maximum Heart Rate Achieved': {
            'advice': "A lower max HR during exercise may indicate risk.",
            'lifestyle': "Regular aerobic exercise can improve your max heart rate.",
            'medication': None
        },
        'Exercise Induced Chest Pain': {
            'advice': "Absence of pain during exercise is ideal.",
            'lifestyle': "Stress management and regular exercise can help reduce chest pain.",
            'medication': "Consult a doctor for appropriate medication if needed."
        },
        'Exercise-related ST Depression': {
            'advice': "Lower values are better. Aim for less than 1 mm.",
            'lifestyle': "Reducing stress and regular exercise are key.",
            'medication': "Consult with a doctor for medications that can help manage heart health."
        },
        'ST Segment Response to Exercise': {
            'advice': "A flat or downsloping response may indicate higher risk.",
            'lifestyle': "Regular cardiac exercises and stress tests are important.",
            'medication': None
        }
    }

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

            # List key factors contributing to heart disease risk
            st.write("### Key factors contributing to heart disease risk:")
            for feature, info in feature_advice.items():
                if feature in ['Age', 'Sex', 'Resting ECG Results', 'ST Segment Response to Exercise']:
                    continue  # Skip these as they are not actionable
                st.write(f"**{feature}:** {info['advice']}")
                st.write(f"  - *Lifestyle Change:* {info['lifestyle']}")
                if info['medication']:
                    st.write(f"  - *Possible Medication:* {info['medication']}")
        else:
            st.success('The model predicts no heart disease.')

if __name__ == '__main__':
    main()
