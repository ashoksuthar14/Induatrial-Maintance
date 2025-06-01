# Predictive Maintenance Analysis Application

This Streamlit application predicts the Remaining Useful Life (RUL) of machines and provides maintenance recommendations using AI analysis.

## Features

- Interactive UI for inputting machine parameters
- Real-time RUL prediction using a trained Random Forest model
- AI-powered maintenance analysis using Google's Gemini API
- Visual representation of predictions
- Sector-specific analysis

## Setup Instructions

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure you have the trained model file (`random_forest_predictive_maintenance_model.pkl`) in the same directory as the application.

3. Run the Streamlit application:
```bash
streamlit run app.py
```

## Usage

1. Enter the machine parameters in the input fields
2. Select the appropriate sector
3. Click "Predict RUL and Analyze" to get:
   - Predicted Remaining Useful Life
   - AI-generated maintenance recommendations
   - Visual representation of the prediction

## Note

The application uses the Gemini API for analysis. The API key is already configured in the application. 