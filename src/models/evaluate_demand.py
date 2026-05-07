import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.models.train_ltsm import prepare_data
from src.data_generation import generate_contextual_data
from src.features import calculate_derived_features

def evaluate_model():
    # 1. Load artifacts
    model = load_model('models/lstm_time_specialist.keras')
    scaler = joblib.load('models/scaler.gz')
    
    # 2. Generate "Unseen" Test Data (to see how it performs on new days)
    df_test = generate_contextual_data(days=10)
    df_test = calculate_derived_features(df_test)
    X_test, y_test, _ = prepare_data(df_test) 
    
    # 3. Predict
    predictions = model.predict(X_test)
    
    # 4. Calculate Metrics
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    print(f"--- Phase 2 Evaluation Metrics ---")
    print(f"RMSE: {rmse:.2f} kW")
    print(f"MAE:  {mae:.2f} kW")
    print(f"R2 Score: {r2:.2f}")

if __name__ == "__main__":
    evaluate_model()