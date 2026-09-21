import streamlit as st
import numpy as np
import joblib

# load model
model = joblib.load('iris_model.pkl')

# page title
st.title('Iris Flower Prediction App')

st.header('Enter the measurements of the Iris flower:')

# input labels
sepal_length = st.number_input(
    'Sepal Length (cm)', min_value=0.0, max_value=10.0, value=5.0, step=0.1
)

sepal_width = st.number_input(
    'Sepal Width (cm)', min_value=0.0, max_value=10.0, value=3.0, step=0.1
)

petal_length = st.number_input(
    'Petal Length (cm)', min_value=0.0, max_value=8.0, value=4.0, step=0.1
)

petal_width = st.number_input(
    'Petal Width (cm)', min_value=0.0, max_value=10.0, value=1.0, step=0.1
)
