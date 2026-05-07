from xgboost import XGBRegressor
import joblib

def train_context_specialist(df):
    # These features are "Tabular" and don't need time-sequences 
    features = ['temp_celsius', 'is_weekend', 'grid_headroom_kw']
    X = df[features]
    y = df['total_load_kw']
    
    model = XGBRegressor(n_estimators=100, learning_rate=0.05)
    model.fit(X, y)
    
    model.save_model('models/xgb_context_specialist.json')
    print("Context-Specialist (XGBoost) Trained and Saved.")