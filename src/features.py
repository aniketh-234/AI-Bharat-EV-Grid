import random

def calculate_derived_features(df):
    # H = Capacity - (CurrentLoad + 10% Safety Margin)
    # Using LaTeX for technical documentation: $$H = C_{total} - (L_{base} + M_{safety})$$
    safety_margin = df['transformer_capacity_kw'] * 0.10
    df['grid_headroom_kw'] = df['transformer_capacity_kw'] - (df['total_load_kw'] + safety_margin)
    df['utilization_ratio'] = (df['home_ev_kw'] + df['public_ev_kw']) / df['transformer_capacity_kw']
    df['ev_growth_rate'] = df['total_load_kw'].pct_change(periods=24).fillna(0)
    return df

def apply_h3_masking(df):
    """Simulates 4 specific Bengaluru zones for the presentation map."""
    bengaluru_hexes = [
        "896014dabffffff", "896014da1ffffff", 
        "896014da5ffffff", "896016091ffffff"
    ]
    df['h3_zone_id'] = [random.choice(bengaluru_hexes) for _ in range(len(df))]
    return df