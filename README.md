# Diabetes Prediction Web App

An interactive web application that predicts the likelihood of diabetes using health data, built with **Python**, **Streamlit**, and **scikit-learn**.



## Project Overview

This project uses the **Pima Indians Diabetes Dataset** from Kaggle to train a **Logistic Regression** model that predicts diabetes based on several health indicators such as:

- Pregnancies  
- Glucose  
- Blood Pressure  
- Skin Thickness  
- Insulin  
- BMI  
- Diabetes Pedigree Function  
- Age  

The app provides an easy-to-use interface to input these parameters and get real-time predictions. Additionally, it includes a feature importance chart to visualize which factors most influence the model's decisions.



## Features

- Diabetes risk prediction using Logistic Regression  
- User-friendly input form for health metrics  
- Visual feature importance chart with Matplotlib  
- Clean and responsive UI powered by Streamlit  
- Educational sidebar explaining the app and model  



## 🛠Technologies Used

- Python 3.12  
- Streamlit  
- scikit-learn  
- NumPy  
- Matplotlib  



## Live Demo

The app is deployed and accessible on Streamlit Community Cloud:

https://diabetesprediction-matafuxvleguocdkidgnlm.streamlit.app/



## Getting Started

### Prerequisites

- Python 3.7 or higher  
- `pip` package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/diabetes-prediction-app.git
   cd diabetes-prediction-app
2.	Create and activate a virtual environment (optional but recommended):
3.	python -m venv venv
4.	source venv/bin/activate   # On Windows: venv\Scripts\activate
5.	Install dependencies:
6.	pip install -r requirements.txt
7.	Run the app:
8.	streamlit run app.py

 Usage
•	Enter the following health parameters on the sidebar (you can use these sample values to test the app):
Parameter	Example Value	Description
Pregnancies	2	Number of times pregnant
Glucose	120	Plasma glucose concentration (mg/dL)
BloodPressure	70	Diastolic blood pressure (mm Hg)
SkinThickness	30	Triceps skinfold thickness (mm)
Insulin	100	2-Hour serum insulin (mu U/ml)
BMI	28.5	Body mass index (weight in kg/(height in m)^2)
DiabetesPedigreeFunction	0.5	Diabetes pedigree function (genetic risk)
Age	30	Age in years

•	Click the Predict button to see the diabetes prediction result.
•	Expand the "Show Feature Importance" section to view which features influence the prediction.

Project Structure
├── app.py                     # Main Streamlit app
├── diabetes_model.pkl         # Trained Logistic Regression model
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── diabetes_prediction_proj   # Project Notebook


 
