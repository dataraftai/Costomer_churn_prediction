from fastapi import FastAPI
from pydantic import BaseModel

import numpy as np
import pandas as pd
import joblib

with open ("costomer_churn_pipline.pkl","rb") as f:
    model = joblib.load(f)
