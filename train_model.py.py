import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

def train_model():
    # Load data
    df = pd.read_parquet("../data/processed/chlorophyll_data.parquet")
    
    # Features and target
    X = df[['latitude', 'longitude', 'chl_anomaly']]
    y = df['log_chl']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Initialize and train model
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    
    # Save model
    joblib.dump(model, "../models/rf_chl_model.pkl")
    print("Model trained and saved")
    
    return model

if __name__ == "__main__":
    train_model()