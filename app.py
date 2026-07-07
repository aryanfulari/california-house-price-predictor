import joblib
import numpy as np
import streamlit as st

# ----------------------------
# Load trained model
# ----------------------------

model = joblib.load("model/house_price_model.pkl")

st.title("🏡 California House Price Predictor")

st.write(
    "Enter the house details below and click Predict."
)

# ----------------------------
# User Inputs
# ----------------------------

med_inc = st.number_input(
    "Median Income",
    min_value=0.0,
    value=3.5,
)

house_age = st.number_input(
    "House Age",
    min_value=1.0,
    value=25.0,
)

ave_rooms = st.number_input(
    "Average Rooms",
    min_value=1.0,
    value=5.0,
)

ave_bedrooms = st.number_input(
    "Average Bedrooms",
    min_value=0.0,
    value=1.0,
)

population = st.number_input(
    "Population",
    min_value=1.0,
    value=1000.0,
)

ave_occup = st.number_input(
    "Average Occupancy",
    min_value=1.0,
    value=3.0,
)

latitude = st.number_input(
    "Latitude",
    value=34.0,
)

longitude = st.number_input(
    "Longitude",
    value=-118.0,
)

# ----------------------------
# Prediction
# ----------------------------

if st.button("Predict"):

    features = np.array([
        [
            med_inc,
            house_age,
            ave_rooms,
            ave_bedrooms,
            population,
            ave_occup,
            latitude,
            longitude,
        ]
    ])

    prediction = model.predict(features)

    st.success(
        f"Predicted House Price: ${prediction[0] * 100000:,.2f}"
    )