AI-Based EV Charging Optimization & Infrastructure Planning for BESCOM

SmartCharge AI is a decision-support system designed to help optimize EV charging demand and plan charging infrastructure efficiently for smart grid management.

The system predicts EV charging demand across city zones, schedules charging to reduce peak load stress, and recommends optimal locations for new EV charging stations — all without modifying existing BESCOM infrastructure.

🚀 Problem Statement

Rapid EV adoption in Bengaluru is creating:

Evening charging peaks
Localized grid overloads
Uneven charging infrastructure demand

Unmanaged charging can lead to:

Transformer stress
Poor load balancing
Long charging wait times

This project provides an AI-driven solution for:

EV demand prediction
Smart charging scheduling
Infrastructure planning
🎯 Objectives
Part A — Demand Prediction & Scheduling
Predict EV charging demand by time and location
Detect peak load periods
Shift charging to off-peak hours
Reduce grid stress
Part B — Infrastructure Planning
Identify high-demand EV zones
Recommend optimal charging station locations
Consider:
Demand growth
Existing infrastructure
Grid capacity
🏗️ System Architecture
Data Simulation
      ↓
Preprocessing & Feature Engineering
      ↓
Demand Prediction Model
      ↓
Smart Charging Scheduler
      ↓
Infrastructure Planning Engine
      ↓
Visualization Dashboard
📌 Key Features
🔹 Demand Prediction
Predicts EV charging demand by:
Time
Zone
EV density
🔹 Smart Scheduling
Detects peak load conditions
Shifts flexible charging to off-peak hours
Balances grid load
🔹 Infrastructure Planning
Detects charging demand hotspots
Recommends new station locations
Considers grid constraints
🔹 Dashboard
Demand heatmaps
Load balancing graphs
Infrastructure recommendation maps
🧠 Technologies Used
Python
Scikit-learn
XGBoost
Pandas
Streamlit
Folium
Plotly
📂 Project Structure
src/
 ├── data_generation.py
 ├── features.py
 ├── scheduler.py
 ├── infrastructure_planner.py
 ├── visualization.py
 │
 └── models/
      ├── demand_predictor.py
      └── train.py
▶️ Workflow
1. Generate Synthetic Dataset
python src/data_generation.py
2. Train Demand Prediction Model
python src/models/train.py
3. Run Smart Scheduler
python src/scheduler.py
4. Run Infrastructure Planner
python src/infrastructure_planner.py
5. Launch Dashboard
streamlit run dashboard/app.py
📊 Expected Outputs
EV demand forecasting
Peak load reduction
Optimized charging schedules
Charging station recommendations
Grid-aware planning insights
✅ Evaluation Metrics
Peak load reduction
Grid utilization improvement
Demand prediction accuracy
Station utilization improvement
🔐 Constraints Followed

✅ No modification to existing BESCOM systems
✅ Uses masked/synthetic data
✅ Explainable recommendations
✅ Grid-aware decision support

🌍 Impact

SmartCharge AI helps:

Reduce grid stress
Improve charging accessibility
Support scalable EV adoption
Enable smarter infrastructure planning
🏆 Developed For

AI for EV Charging Optimization & Infrastructure Planning — BESCOM Hackathon
