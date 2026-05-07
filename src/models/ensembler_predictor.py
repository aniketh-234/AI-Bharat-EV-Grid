import joblib
import numpy as np
from tensorflow.keras.models import load_model
from xgboost import XGBRegressor

class GridEnsemble:
    def __init__(self):
        self.lstm = load_model('models/lstm_time_specialist.keras')
        self.xgb = XGBRegressor()
        self.xgb.load_model('models/xgb_context_specialist.json')
        self.scaler = joblib.load('models/scaler.gz')

    def predict(self, window_data, context_features):
        # 1. Get predictions from both specialists
        p_lstm = self.lstm.predict(window_data, verbose=0)
        p_xgb = self.xgb.predict(context_features)
        
        # 2. Hybrid Stacking (Simple Averaging for now to move fast)
        # In a full Meta-Learner, you'd use a Ridge Regressor here 
        final_prediction = (p_lstm.flatten() + p_xgb) / 2
        return final_prediction