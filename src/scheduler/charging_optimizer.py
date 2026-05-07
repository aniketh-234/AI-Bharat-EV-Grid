import pandas as pd

def schedule_charging(predicted_load, capacity, safety_margin=0.10):
    """
    Implements Phase 3: Detects peaks and identifies 'Safe Zones' for charging.
    """
    # 1. Calculate Grid Headroom formula [cite: 21]
    # Headroom = Total Capacity - (Current Load + Safety Margin)
    limit = capacity * (1 - safety_margin)
    headroom = limit - predicted_load
    
    # 2. Identify Critical Peaks
    is_peak = predicted_load > limit
    
    # 3. Scheduling Recommendation
    recommendation = []
    for h in headroom:
        if h < 0:
            recommendation.append("SHIFT: Critical Peak Detected")
        elif h < (capacity * 0.2):
            recommendation.append("CAUTION: Low Headroom")
        else:
            recommendation.append("SAFE: Optimal Charging Window")
            
    return recommendation, headroom