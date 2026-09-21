import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("iris_model.pkl")

# Page title
st.title("Iris Flower Prediction App")

st.header("Enter the measurements of the Iris flower:")

# Input fields
sepal_length = st.number_input(
    "Sepal Length (cm)",
    min_value=0.0,
    max_value=10.0,
    value=5.0,
    step=0.1
)

sepal_width = st.number_input(
    "Sepal Width (cm)",
    min_value=0.0,
    max_value=10.0,
    value=3.0,
    step=0.1
)

petal_length = st.number_input(
    "Petal Length (cm)",
    min_value=0.0,
    max_value=8.0,
    value=4.0,
    step=0.1
)

petal_width = st.number_input(
    "Petal Width (cm)",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)

# Prediction button
if st.button("Predict"):

    # Prepare input data
    input_data = np.array([
        [sepal_length, sepal_width, petal_length, petal_width]
    ])

    # Make prediction
    prediction = model.predict(input_data)

    # Display prediction
    if prediction[0] == 0:
        flower = "Iris Setosa"
    elif prediction[0] == 1:
        flower = "Iris Versicolor"
    else:
        flower = "Iris Virginica"

    st.success(f"🌸 Predicted Flower: {flower}")
