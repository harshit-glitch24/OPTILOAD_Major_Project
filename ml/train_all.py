# ==============================================================================================
# 🚀 MASTER ML TRAINING PIPELINE LAUNCHER (ml/train_all.py)
# ----------------------------------------------------------------------------------------------
# PURPOSE : Single-command reproducible execution of all 5 production machine learning models:
#           1. Delay Predictor (HistGradientBoosting on 180k Kaggle DataCo records)
#           2. Freight Cost Regressor (HistGradientBoosting on 10k USAID records)
#           3. Demand Forecaster (PyTorch 2-Layer LSTM on 913k Store observations)
#           4. IoT Anomaly Detector (Isolation Forest on 7.2k NAB telemetry readings)
#           5. Corridor Topology Embedder (GraphSAGE GNN on Indian Highway GIS graph)
# USAGE   : python ml/train_all.py
# ==============================================================================================

import os
import sys
from pathlib import Path

# Ensure root directory is in sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from ml.train_all_real import metrics_report

if __name__ == "__main__":
    print("🚀 Executing production LogiLoad AI/ML Model Training Pipeline on Real Kaggle & Open Datasets...")
    import ml.train_all_real
