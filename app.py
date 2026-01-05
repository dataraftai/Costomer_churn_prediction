from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input_pydantic import UserInput,COLUMN_MAPPING
from schema.prediction_responce import PredictionResponce 
from model.predict import MODEL_VERSION,model

import numpy as np
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to the Customer Churn Prediction API",
        "description": "Predicts whether a telecom customer will churn",
        "endpoints": {
            "/predict": "Churn prediction endpoint",
            "/docs": "Swagger documentation"
            }
    }

@app.get("/health")
def health_check():
    return {
        "status" : "ok",
        "version" : MODEL_VERSION,
        "model_loaded" : model is not None
    }

@app.post("/predict",response_model=PredictionResponce)
def predict_churn(data:UserInput):

    input_df = pd.DataFrame([data.model_dump()])   
    input_df.rename(columns=COLUMN_MAPPING, inplace=True)

    try :
        prediction = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1]

        return JSONResponse(status_code=200,content={"predicted":int(prediction),
        "churn_label" : "Churn" if prediction == 1 else "No Churn",
        "churn_probability":round(float(prob),4)
        })
    
    except Exception as e:

        return JSONResponse(status_code=500,content=str(e))