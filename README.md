Heart Disease Detection App
This tool is an app built upon testing and leveraging machine learning models learned in this class. This app is catered towards doctors based on multiple risk factors that doctors will have access to such as Age, cholesterol levels, and blood pressure to help identify whether or not a patient is at risk. A tool like this will not only help a doctor make smarter decisions faster, it will allow them to know what features a patient should spend more time focusing on improving.


You may need these dependencies:
pip install streamlit
pip install pandas joblib
pip install -U scikit-learn

In order to run this file you will need to run the following:
python train_model.py     #This will train the model we use and create a random_forest_11_features.joblib file that will be used
streamlit run your_app.py      #This will open up the app in a new browser
