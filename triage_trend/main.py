from typing import Any, Dict

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

from triage_trend.data_service.feature_map import feature_map
from triage_trend.data_service.get_data import get_data

MODEL_PATH = "./model/gb_model.pkl"

model = joblib.load(MODEL_PATH)
app = FastAPI()


class PredictionRequest(BaseModel):
    date: str  # Date in 'YYYY-MM-DD' format


class PredictionResponse(BaseModel):
    prediction: float
    featuresUsed: Dict[str, Any]


@app.post("/predict", response_model=PredictionResponse)
async def predict(data: PredictionRequest):
    features = get_data(data.date)
    input_df = pd.DataFrame([features])
    input_df = input_df[model.named_steps['preprocessor'].feature_names_in_]
    prediction = model.predict(input_df)
    features_camel_case = {feature_map.get(k, k): v for k, v in features.items()}

    return PredictionResponse(
        prediction=prediction[0], featuresUsed=features_camel_case
    )
