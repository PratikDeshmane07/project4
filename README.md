# Heart Disease Prediction App Project

## Overview

In this project, we focused on leveraging machine learning to predict heart disease, transforming raw data into actionable insights and a practical application. Our journey from data processing to model deployment showcases the blend of analytical rigor and technical proficiency.

## Repository Structure

- `App Development`: Contains the Streamlit-based application, utilizing joblib for model deployment.
- `Model Optimization`: Features scikit-learn for model tuning, with a focus on GridSearchCV for parameter optimization.
  - Final model performance metrics:
    - Accuracy: 88.04%
    - Precision: 89.72%
    - Recall: 89.72%
    - F1 Score: 89.72%
    - AUC-ROC: 87.72%
    - R2 Score: 58.37%
- `Model Testing`: Evaluates a range of models to determine the most effective:
  - Decision Trees
  - Logistic Regression
  - RandomForest Classifier
  - XGBoost
- `Neural Network Models`: Contains neural network models designed for pattern recognition and predictions.
- `Visualizations`: Houses visual outputs from matplotlib and seaborn for data representation.
- `archive`: A collection of supplementary and exploratory files.
- `data`: Managed with pandas, includes both raw and processed datasets, demonstrating extensive data processing.

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
