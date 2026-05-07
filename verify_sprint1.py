from src.data_generation import generate_contextual_data
from src.features import calculate_derived_features, apply_h3_masking

# 1. Generate Raw Data
raw_data = generate_contextual_data(days=5)

# 2. Refine Data
refined_data = calculate_derived_features(raw_data)
final_data = apply_h3_masking(refined_data)

print(final_data[['timestamp', 'grid_headroom_kw', 'utilization_ratio', 'h3_zone_id']].head())
print("\nSprint 1 Execution Successful: Features Refined and Masked.")