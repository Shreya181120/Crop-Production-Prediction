# 🌾 Crop Production Prediction Using Machine Learning

## Project Overview
This project predicts crop production using a trained **Random Forest Regression** model. It includes a Streamlit web application where users can select a crop, choose a year, enter an area value, and obtain a predicted production value.

## Features
- Interactive Streamlit web application
- Crop selection and year-based inputs
- Production prediction using Random Forest Regression
- Data preprocessing and exploratory data analysis (EDA)
- Saved machine learning model and crop encoder

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle
- Jupyter Notebook

## Model Information
- **Algorithm:** Random Forest Regressor
- **Number of estimators:** 100
- **Features:** Crop Code, Year Code, Area
- **Evaluation metrics:** MAE, RMSE, and R²

The model's reported evaluation results are based on the prepared dataset and test split. Predictions are exploratory and should not be treated as verified real-world forecasts.

## Dataset
The prepared dataset covers crop records from 2006–07 to 2010–11. Measurement units should be verified before interpreting production values.

## How to Run Locally
1. Clone or download this repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the application using `python -m streamlit run app.py`.
4. Open the local URL shown in the terminal.

## Project Files
- `Agriculture.ipynb` — data analysis and model development
- `app.py` — Streamlit application
- `crop_production_model.pkl` — trained model
- `crop_encoder.pkl` — crop label encoder
- CSV files — source datasets

## Disclaimer
This project is intended for educational and demonstration purposes. Prediction quality depends on the dataset, its coverage, and the selected inputs.
