import streamlit as st
import pickle
import numpy as np

# Load the trained CatBoost model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("🔥 Calorie Burnt Prediction App")

st.write("Enter your details below to predict the calories burnt.")

# User Inputs (matching the dataset feature order)
age = st.number_input("Age", min_value=10, max_value=100, value=25)
height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0)
weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
duration = st.number_input("Workout Duration (minutes)", min_value=5, max_value=300, value=60)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=50, max_value=200, value=100)
body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=37.0)

# Gender selection dropdown (1 = Male, 0 = Female) 
gender = st.selectbox("Gender", ["Male", "Female"])
gender_encoded = 1.0 if gender == "Male" else 0.0  # Gender_male column

# Predict Button
if st.button("Predict Calories Burnt"):
    # Arrange input data in the correct order
    input_data = np.array([[age, height, weight, duration, heart_rate, body_temp, gender_encoded]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display result
    st.success(f"🔥 Estimated Calories Burnt: {prediction[0]:.2f} kcal")