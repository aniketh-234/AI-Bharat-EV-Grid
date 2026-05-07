import pandas as pd
import numpy as np

def generate_contextual_data(days=30):
    time_index = pd.date_range(start="2026-05-01", periods=days*24, freq='h')
    
    # Contextual Variables
    is_weekend = time_index.weekday >= 5
    # Simulate temperature (higher temp = more AC usage = higher base load)
    temp = 25 + 10 * np.sin(np.pi * (time_index.hour - 12) / 12) + np.random.normal(0, 2, len(time_index))
    
    # 1. Base Load (Impacted by Temp and Time)
    base_load = 200 + (temp * 5) + (100 * np.sin(np.pi * (time_index.hour - 6) / 12))
    
    # 2. EV Load (Differentiating between Home and Public chargers)
    # Home chargers: Night bias | Public chargers: Day bias
    home_ev = np.where((time_index.hour >= 19) | (time_index.hour <= 7), np.random.normal(100, 15), 10)
    public_ev = np.where((time_index.hour >= 10) & (time_index.hour <= 17), np.random.normal(80, 10), 5)
    
    df = pd.DataFrame({
        'timestamp': time_index,
        'temp_celsius': temp,
        'is_weekend': is_weekend.astype(int),
        'base_load_kw': base_load,
        'home_ev_kw': home_ev,
        'public_ev_kw': public_ev,
        'total_load_kw': base_load + home_ev + public_ev,
        'transformer_capacity_kw': 500  # Assume a standard 500kW DTR
    })
    return df