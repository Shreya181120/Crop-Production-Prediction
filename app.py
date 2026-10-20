
import pickle
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Crop Production Prediction",
    page_icon="🌾",
    layout="centered"
)

@st.cache_resource
def load_files():
    with open("crop_production_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("crop_encoder.pkl", "rb") as f:
        encoder = pickle.load(f)

    return model, encoder

try:
    model, encoder = load_files()
except Exception as e:
    st.error(f"Model files could not be loaded: {e}")
    st.stop()

st.title("🌾 Crop Production Prediction")
st.write(
    "Predict crop production using a trained "
    "Random Forest Regression model."
)

st.info(
    "The dataset covers 2006–07 to 2010–11. "
    "Predictions are exploratory, and measurement "
    "units have not yet been verified."
)

crop = st.selectbox(
    "Select Crop",
    list(encoder.classes_)
)

year = st.selectbox(
    "Select Year",
    [2006, 2007, 2008, 2009, 2010]
)

area = st.number_input(
    "Enter Area (dataset units)",
    min_value=0.0,
    value=100.0,
    step=1.0
)

if st.button("Predict Production"):
    crop_code = int(encoder.transform([crop])[0])

    input_data = pd.DataFrame(
        [[crop_code, year, area]],
        columns=["Crop_Code", "Year_Code", "Area"]
    )

    prediction = float(model.predict(input_data)[0])

    st.success(
        f"Predicted Production Value: {prediction:.2f}"
    )
