import joblib
import pandas as pd
import numpy as np

def predict(lat, lon, anomaly):
    # Load model
    model = joblib.load("../models/rf_chl_model.pkl")
    
    # Create input array
    input_data = pd.DataFrame({
        'latitude': [lat],
        'longitude': [lon],
        'chl_anomaly': [anomaly]
    })
    
    # Make prediction
    log_pred = model.predict(input_data)[0]
    prediction = np.exp(log_pred)  # Convert back from log scale
    return prediction

if __name__ == "__main__":
    # Example prediction (San Francisco coordinates)
    print(f"Predicted Chlorophyll-a: {predict(37.7, -122.4, 0.15):.4f} mg/m³")