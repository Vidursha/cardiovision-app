❤️ CardioVision
AI-Powered Cardiovascular Disease Risk Prediction System

📖 Project Background

Cardiovascular diseases (CVDs) are among the leading causes of death worldwide. Many heart-related conditions develop silently and are often detected only at advanced stages. Early identification of at-risk individuals is critical for prevention, timely intervention, and improved patient outcomes.

CardioVision is an AI-powered web application designed to predict the probability of cardiovascular disease using clinical measurements and lifestyle factors. By leveraging machine learning techniques, the system delivers fast, data-driven risk assessments through an intuitive web interface.

📊 Dataset (Brief Introduction)

This project uses the Cardiovascular Disease Dataset from Kaggle:

🔗 Dataset Link:
https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset

Dataset Overview

Total Records: 70,000 patients

Target Variable:

1 → Presence of cardiovascular disease

0 → Absence of cardiovascular disease

Feature Categories

Objective Features:
Age, Gender, Height, Weight

Clinical Examination Features:
Systolic Blood Pressure, Diastolic Blood Pressure, Cholesterol, Glucose

Lifestyle Features:
Smoking Status, Alcohol Intake, Physical Activity

🎯 Business Goals

The key objectives of the CardioVision system are:

Early Detection – Identify individuals at risk of cardiovascular disease.

Clinical Decision Support – Assist healthcare professionals in patient prioritization.

Cost & Time Efficiency – Reduce dependence on expensive diagnostic tests for initial screening.

Accessibility – Provide a simple and accessible web-based risk assessment tool.

⚙️ What’s Implemented
🔹 Data Preparation

Removal of duplicate records

Handling missing values

Filtering unrealistic and impossible blood pressure values

Data consistency checks for clinical validity

🔹 Feature Engineering

Conversion of age from days to years

BMI calculation using height and weight

Encoding categorical variables

Feature scaling using StandardScaler for optimal model performance

🔹 Predictive Modeling

The following classification models were trained and evaluated:

Logistic Regression

Decision Tree Classifier

Random Forest Classifier

Each model was trained using the same preprocessed dataset to ensure fair comparison.

🔹 Model Evaluation

Performance measured using accuracy, precision, recall, and ROC–AUC

ROC–AUC prioritized due to class imbalance

Comparative analysis conducted to identify the most robust model

🔹 Best Model Selection

🏆 Selected Model: Random Forest Classifier
📈 ROC–AUC Score: 0.7862

Reason for Selection:

Highest ROC–AUC score among tested models

Better generalization on unseen data

Reduced overfitting compared to a single decision tree

Stable performance across diverse patient profiles

The final model was saved using joblib and deployed in the application.

🔹 Visualization & UI

Interactive UI built using Streamlit

Real-time risk probability gauge

Clear visual indicators for Low Risk and High Risk

Dynamic input controls (sliders, dropdowns)

Support for Single Prediction and Batch Prediction (CSV upload)

🌐 Web Application & Deployment

Frontend developed using Streamlit

Integrated trained ML model for real-time inference

Deployed on Streamlit Community Cloud

🔗 Live App:
https://cardiovision-app-c7w9afptfcoddi6uttbbfu.streamlit.app/

🛠️ Tools & Technologies

Programming Language: Python 3.9+

Frontend Framework: Streamlit

Data Processing: Pandas, NumPy

Machine Learning: Scikit-learn

Visualization: Plotly, Matplotlib

Model Persistence: Joblib

Version Control: Git & GitHub

Deployment Platform: Streamlit Community Cloud
