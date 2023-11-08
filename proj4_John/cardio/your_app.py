import streamlit as st
import numpy as np
import joblib

# Load the trained Random Forest model
model = joblib.load('random_forest_cv_model.joblib')

# Define the structure of the web app
def main():
    # Set page config to widen the app and set a fun icon and title
    st.set_page_config(page_title='Heart Health Predictor', page_icon=":heart:", layout="wide")

    # Add a header and an image
    st.write("""
    # Heart Health Predictor :heart:
    Welcome to the Cardiovascular Disease Prediction App. Please enter the following information to predict cardiovascular disease risk.
    """)

    # Create two columns for inputs and the model output
    col1, col2 = st.columns(2)

    # Inputs in the left column
    with col1:
        st.header("Input Features")
        age = st.number_input('Age', min_value=0, max_value=120, value=30)
        sex = st.selectbox('Sex', options=['Male', 'Female'])
        chest_pain_type = st.selectbox('Chest Pain Type', options=['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
        resting_bp = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0)
        cholesterol = st.number_input('Cholesterol (mg/dl)', min_value=0)
        fasting_bs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=['No', 'Yes'])
        resting_ecg = st.selectbox('Resting Electrocardiogram Results', options=['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])
        max_hr = st.number_input('Maximum Heart Rate Achieved', min_value=0)
        exercise_angina = st.selectbox('Exercise Induced Angina', options=['No', 'Yes'])
        oldpeak = st.number_input('ST Depression Induced by Exercise Relative to Rest')
        st_slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=['Upsloping', 'Flat', 'Downsloping'])

    # Button to make prediction and output in the right column
    with col2:
        st.header("Prediction Results")
        if st.button('Predict'):
            # Pre-process inputs
            input_data = np.array([[age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs,
                                    resting_ecg, max_hr, exercise_angina, oldpeak, st_slope]])
            # Use your preprocessing here to match the model's expected input
            # For example, you might need to one-hot encode the inputs similarly to the training process

            # Make a prediction
            prediction = model.predict(input_data)

            if prediction[0] == 1:
                st.error('The model predicts a risk of cardiovascular disease.')
            else:
                st.success('The model predicts a low risk of cardiovascular disease.')

    # Add some footer notes about health
    st.info("""
    **Note:** This prediction is based on machine learning models and is not a substitute for professional medical advice.
    For any health-related concerns, please consult a healthcare professional.
    """)

    # Add a sidebar with contact info or additional details
    with st.sidebar:
        st.header("About")
        st.write("""
        This app uses a Random Forest model to predict the likelihood of a patient having cardiovascular disease based on various health metrics. 
        The model was trained on a dataset from the UCI Machine Learning Repository.
        """)
        st.write("## Contact Us")
        st.write("If you have any questions, please reach out to us at [email](mailto:your_email@example.com).")

if __name__ == '__main__':
    main()
