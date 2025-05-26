import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt

# Load trained model
with open('diabetes_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Set Streamlit page config
st.set_page_config(page_title="Diabetes Predictor", layout="centered")

# --- Custom CSS ---
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #0099ff;
        color: white;
        padding: 0.6em 1.5em;
        font-weight: bold;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #007acc;
    }
    .result {
        font-size: 1.2em;
        font-weight: bold;
        padding: 1em;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("About")
st.sidebar.info("""
This app uses a machine learning model trained on the **Pima Indians Diabetes Dataset** to predict the likelihood of diabetes.

### Model Info:
- Type: Logistic Regression  
- Inputs:
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age

Built with **Streamlit** and **scikit-learn**
""")


# --- App Title & Description ---
st.title("Diabetes Prediction App")
st.write("Fill in the information below to check if someone is at risk of diabetes:")

# --- User Inputs ---
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, step=1)
glucose = st.number_input("Glucose", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0, format="%.1f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
age = st.number_input("Age", min_value=0, max_value=120)

# --- Prediction ---
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.markdown('<div class="result" style="background-color:#ffcccc;">⚠️ The person <strong>is likely diabetic</strong>.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result" style="background-color:#ccffcc;">✅ The person <strong>is not diabetic</strong>.</div>', unsafe_allow_html=True)

# --- Feature Importance Chart ---
with st.expander("Show Feature Importance"):
    features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
                'BMI', 'DiabetesPedigreeFunction', 'Age']
    importances = np.abs(model.coef_[0])  # works for Logistic Regression

    fig, ax = plt.subplots()
    ax.barh(features, importances, color='skyblue')
    ax.set_xlabel("Coefficient Magnitude")
    ax.set_title("Feature Importance (Logistic Regression)")
    st.pyplot(fig)
