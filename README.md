# Heart Disease Prediction App Project

## Overview
In this project, we focused on leveraging machine learning to predict heart disease, transforming raw data into actionable insights and a practical application. Our journey from data processing to model deployment showcases the blend of analytical rigor and technical proficiency.

## Repository Structure
- `App Development`: The culmination of our work, this folder contains a Streamlit-based application, reflecting the practical application of our predictive models. The deployment process utilized `joblib` to load trained models efficiently.
- `Model Optimization`: Here, we delve into the fine-tuning of our machine learning models, employing `scikit-learn` and specifically `GridSearchCV` for exhaustive parameter testing to ensure peak model performance. The final model boasts an accuracy of 0.8804, precision of 0.8972, and other key metrics such as an AUC-ROC of 0.8772.
- `Model Testing`: A diverse range of models including Decision Trees, Logistic Regression, RandomForest Classifier, Support Vector Machines, and XGBoost were evaluated to determine the most effective approach for our dataset.
- `Neural Network Models`: Features the neural network models that form the core predictive engine of the application, designed to understand complex patterns and make accurate predictions.
- `Visualizations`: This folder houses the visual outputs that make our data analysis accessible and insightful, utilizing `matplotlib` and `seaborn` for graphical representation.
- `archive`: A collection of supplementary data and exploratory files that have supported the project's development.
- `data`: Central to the project, this folder contains datasets managed and manipulated with `pandas`, showcasing extensive data cleaning, preprocessing, and preparation for modeling.

## Team Members
- Calvin Kleber
- Prachi Shingvi
- Pratik Deshmane
- Mike Strati
- Eric Huynh
- Shridhik John

## Acknowledgments
We extend our appreciation to [UC Berkeley Extension Data Analytics Boot Camp](https://bootcamp.berkeley.edu/data/), which provided the environment that fostered our growth and collaboration.

We are also grateful to the machine learning community for their contributions that inspired our project:
- The "Heart Failure Prediction" Kaggle project by fedesoriano, found at [Heart Failure Prediction](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction), was a significant source of inspiration.
- The original heart disease dataset authors provided a solid foundation for our analysis:
  - Janosi, Andras
  - Steinbrunn, William
  - Pfisterer, Matthias
  - Detrano, Robert

The original dataset, sourced from the UCI Machine Learning Repository and dating back to June 30, 1988, was crucial in our project's development. Further details on the dataset can be found here:

Janosi, Andras; Steinbrunn, William; Pfisterer, Matthias; Detrano, Robert. (1988). Heart Disease. UCI Machine Learning Repository. [https://archive.ics.uci.edu/ml/datasets/heart+disease](https://doi.org/10.24432/C52P4X).
