import pandas as pd
import joblib

with open ("model/costomer_churn_pipline.pkl","rb") as f:
    model = joblib.load(f)

MODEL_VERSION = "1.0.0"
