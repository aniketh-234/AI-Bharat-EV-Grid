import numpy as np
import pandas as pd
import joblib
import os
from sklearn.preprocessing import MinMaxScaler

from src.models.demand_predictor import build_lstm_model
from src.data_generation import generate_contextual_data
from src.features import calculate_derived_features

def prepare_data(df, window_size=24):
    # We use Total_Load_kW and Grid_Headroom as our primary features
    features = df[['total_load_kw', 'grid_headroom_kw']].values
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(features)
    
    X, y = [], []
    for i in range(window_size, len(scaled_data)):
        X.append(scaled_data[i-window_size:i])
        y.append(scaled_data[i, 0]) # Target is the Total_Load_kW
        
    return np.array(X), np.array(y), scaler

if __name__ == "__main__":
    # Ensure the models directory exists
    os.makedirs('models', exist_ok=True)

    # 1. Pipeline: Generate -> Refine -> Window
    print("Generating data...")
    df = generate_contextual_data(days=60) 
    df = calculate_derived_features(df)
    X, y, scaler = prepare_data(df)

    # 2. Build & Train the LSTM (The Time-Specialist)
    print("Starting Training...")
    model = build_lstm_model(input_shape=(X.shape[1], X.shape[2]))
    model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2)

    # 3. Save artifacts for the final Ensemble
    model.save('models/lstm_time_specialist.keras')
    joblib.dump(scaler, 'models/scaler.gz')
    print("Time-Specialist Trained and Saved to models/lstm_time_specialist.keras")