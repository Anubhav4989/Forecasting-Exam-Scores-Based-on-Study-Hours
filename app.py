import streamlit as st
import joblib
import numpy as np

# Set up the web app title
st.title("Divya Jain School of Excellence")
st.subheader("Forecasting Exam Scores Based on Study Hours")

# Load the saved model
with open('Forecasting_Exam_Scores_Based_on_Study_Hours.pkl', 'rb') as file:
    model = joblib.load(file)

# Input for study hours
study_hours = st.number_input("Enter the number of study hours:", min_value=0.0, step=0.5)

# Button to predict
if st.button("Predict Exam Score"):
    # Ensure valid input
    if study_hours >= 0:
        # Reshape input to be a 2D array (for the model)
        prediction = model.predict(np.array([[study_hours]]))[0].round(2)
        st.success(f"Predicted Exam Score: {prediction}")
    else:
        st.error("Study hours cannot be negative!")

# Footer or About Section
st.write("---")
st.write("**Developed by:** Anubhav Kumar Tiwary")