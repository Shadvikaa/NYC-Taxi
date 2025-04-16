import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("fare_prediction_model.pkl")

# Page config
st.set_page_config(page_title="NYC Taxi Fare Predictor 🚖", page_icon="🚕", layout="centered")

# Custom CSS for yellow taxi theme
st.markdown("""
    <style>
    body {
        background-color: #FFFACD;
    }
    .main {
        background-color: #FFFACD;
    }
    .stButton>button {
        background-color: #FFD700;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        border: 2px solid black;
    }
    .stTextInput>div>div>input {
        background-color: #FFF8DC;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.title("🚖 NYC Taxi Fare Predictor")
st.subheader("Estimate your fare in seconds!")

# Inputs
st.markdown("### 📋 Enter Trip Details")

trip_distance = st.number_input("📏 Trip Distance (miles)", min_value=0.0, format="%.2f")
tip_amount = st.number_input("💵 Tip Amount ($)", min_value=0.0, format="%.2f")
total_amount = st.number_input("🧾 Total Amount ($)", min_value=0.0, format="%.2f")

# Predict
if st.button("🧮 Predict Fare"):
    input_data = np.array([[trip_distance, tip_amount, total_amount]])
    prediction = model.predict(input_data)
    st.success(f"🎯 Estimated Fare Amount: **${prediction[0]:.2f}**")
    st.balloons()