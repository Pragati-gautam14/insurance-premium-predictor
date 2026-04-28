import streamlit as st
import pickle
import numpy as np

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🏥 Medical Insurance Premium Predictor")
st.write("Fill in your details to predict your insurance premium!")

# Input fields
age = st.slider("Age", 18, 64, 30)
sex = st.selectbox("Sex", ["Male", "Female"])
bmi = st.number_input("BMI", 15.0, 54.0, 30.0)
children = st.slider("Number of Children", 0, 5, 0)
smoker = st.selectbox("Smoker?", ["No", "Yes"])
region = st.selectbox("Region", ["Southwest", "Southeast", "Northwest", "Northeast"])

# Encode inputs
sex_enc = 1 if sex == "Male" else 0
smoker_enc = 1 if smoker == "Yes" else 0
region_enc = {"Southwest": 0, "Southeast": 1, "Northwest": 2, "Northeast": 3}[region]

# Predict
if st.button("Predict Premium 💰"):
    input_data = np.array([[age, sex_enc, bmi, children, smoker_enc, region_enc]])
    prediction = model.predict(input_data)[0]
    st.success(f"💵 Estimated Insurance Premium: **${prediction:,.2f}**")
    st.balloons()