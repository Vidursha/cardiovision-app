❤️ CardioVision
AI-Powered Cardiovascular Disease Risk Prediction System
📖 Project Background

Cardiovascular diseases (CVDs) are among the leading causes of mortality worldwide. Many heart-related conditions progress silently and are often diagnosed only at advanced stages, making early detection essential for effective prevention and treatment.

CardioVision is an AI-powered web application developed to predict the likelihood of cardiovascular disease using clinical measurements and lifestyle-related factors. By applying machine learning techniques, the system provides fast, reliable, and data-driven risk assessments through a user-friendly web interface.

📊 Dataset 

This project utilizes the Cardiovascular Disease Dataset obtained from Kaggle.

🔗 Dataset Link:
https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset

Dataset Overview

Total Records: 70,000 patient records

Target Variable:

1 – Presence of cardiovascular disease

0 – Absence of cardiovascular disease

Feature Categories

Objective Features: Age, Gender, Height, Weight

Clinical Examination Features: Systolic Blood Pressure, Diastolic Blood Pressure, Cholesterol, Glucose

Lifestyle Features: Smoking Status, Alcohol Intake, Physical Activity

🎯 Business Goals

The primary objectives of the CardioVision system include:

Early Detection
Identifying individuals at potential risk of cardiovascular disease at an early stage.

Clinical Decision Support
Assisting healthcare professionals in prioritizing patients based on predicted risk levels.

Cost and Time Efficiency
Reducing reliance on expensive and time-consuming diagnostic procedures for initial screening.

Accessibility
Providing an easy-to-use, web-based cardiovascular risk assessment tool accessible to a wide audience.

⚙️ What’s Implemented
Data Preparation

Removal of duplicate records

Handling missing values

Filtering unrealistic and physiologically impossible blood pressure values

Ensuring data consistency and clinical validity

Feature Engineering

Conversion of age from days to years

Body Mass Index (BMI) calculation using height and weight

Encoding categorical variables

Feature scaling using StandardScaler to improve model performance

Predictive Modeling

The following classification models were trained and evaluated using the same preprocessed dataset to ensure fair comparison:

Logistic Regression

Decision Tree Classifier

Random Forest Classifier

Model Evaluation

Performance evaluated using accuracy, precision, recall, and ROC–AUC

ROC–AUC prioritized due to class imbalance

Comparative analysis conducted to identify the most reliable model

Best Model Selection

Selected Model: Random Forest Classifier

ROC–AUC Score: 0.7862

Reason for Selection:

Achieved the highest ROC–AUC score among all tested models

Demonstrated strong generalization on unseen data

Reduced overfitting compared to a single decision tree

Stable and consistent performance across diverse patient profiles

The final model was serialized using joblib and integrated into the web application.

Visualization & User Interface

Interactive user interface developed using Streamlit

Real-time cardiovascular risk probability display

Clear visual indicators for Low Risk and High Risk

Dynamic input controls such as sliders and dropdown menus

Support for both Single Prediction and Batch Prediction (CSV upload)

🌐 Web Application & Deployment

Frontend developed using Streamlit

Integrated trained machine learning model for real-time predictions

Deployed on Streamlit Community Cloud

🔗 Live Application:
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
