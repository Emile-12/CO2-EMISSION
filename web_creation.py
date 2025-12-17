import streamlit as st
import pickle
import numpy as np
import os

# Set page configuration
st.set_page_config(page_title="CO₂ Emission Predictor", layout="centered")

st.title("🚗 [25RP21270] CO₂ Emission Prediction App")
st.write("Enter vehicle details to predict CO₂ emissions.")

# Get the path to the model relative to this script
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "25RP21270.sav")

# Load trained model
try:
    with open(model_path, "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found. Make sure 25RP21270.sav is in the same folder as app.py.")
    st.stop()

# User input
volume = st.number_input(
    "Engine Volume (cc)",
    min_value=500,
    max_value=6000,
    step=100
)

weight = st.number_input(
    "Vehicle Weight (kg)",
    min_value=500,
    max_value=3000,
    step=50
)

# Prediction
if st.button("Predict CO₂ Emission"):
    prediction = model.predict([[volume, weight]])
    st.success(f"Predicted CO₂ Emission: {prediction[0]:.2f} g/km")
