import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("calories_model.pkl", "rb"))

# Page config
st.set_page_config(page_title="Calories Burnt Predictor", page_icon="🔥", layout="centered")

# Custom CSS for professional look
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #0e1117;
    color: white;
    text-align: center;
    padding: 10px;
}
a {
    color: #4da6ff;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

# Title Section
st.title("🔥 Calories Burnt Prediction App")
st.markdown("### Predict calories burned based on exercise and body parameters")

st.divider()

# Input Section
st.subheader("Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=1, max_value=100, value=25)
    height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)

with col2:
    duration = st.number_input("Exercise Duration (minutes)", min_value=1, max_value=300, value=30)
    heart_rate = st.number_input("Heart Rate", min_value=50, max_value=200, value=120)
    body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=37.0)

# Convert gender to numeric
gender_num = 0 if gender == "Male" else 1

# Prediction button
if st.button("🔥 Predict Calories Burned"):
    input_data = np.array([[gender_num, age, height, weight, duration, heart_rate, body_temp]])
    prediction = model.predict(input_data)

    st.success(f"✅ Estimated Calories Burned: **{round(prediction[0], 2)} kcal**")

# Footer
st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #0e1117;
    color: white;
    text-align: center;
    padding: 10px;
}
.footer img {
    width: 28px;
    margin: 0 10px;
    vertical-align: middle;
    cursor: pointer;
}
</style>

<div class="footer">
    Developed by <b>Shree Lakshmi</b>
    <a href="mailto:shreelakshmipp@gmail.com">
        <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="Email">
    </a>
    <a href="https://www.linkedin.com/in/shree-lakshmi-b9a769239" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn">
    </a>
</div>
""", unsafe_allow_html=True)
