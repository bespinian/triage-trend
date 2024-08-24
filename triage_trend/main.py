from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Define the path to the saved model
MODEL_PATH = './model/gb_model.pkl'

# Load the model
model = joblib.load(MODEL_PATH)

# Initialize FastAPI app
app = FastAPI()

# Define the request body model
class PredictionRequest(BaseModel):
    Average_Temperature: float
    Max_Temperature: float
    Total_Rain_Duration: float
    Average_Pressure: float
    Average_Global_Radiation: float
    Cloudiness: float
    Moon_Phase: float
    IsVacationAargau: int
    IsVacationZug: int
    IsVacationSchwyz: int
    IsVacationSt_gallen: int
    IsVacationSchaffhausen: int
    IsVacationThurgau: int
    Weekday: int  # Numeric representation of the weekday (0 = Monday, 6 = Sunday)
    IsWeekend: int  # 1 if it's a weekend, 0 otherwise

@app.post("/predict")
async def predict(data: PredictionRequest):
    # Convert the request data into a DataFrame
    input_df = pd.DataFrame([{
        'Average_Temperature': data.Average_Temperature,
        'Max_Temperature': data.Max_Temperature,
        'Total_Rain_Duration': data.Total_Rain_Duration,
        'Average_Pressure': data.Average_Pressure,
        'Average_Global_Radiation': data.Average_Global_Radiation,
        'Cloudiness': data.Cloudiness,
        'Moon Phase (%)': data.Moon_Phase,
        'IsVacationAargau': data.IsVacationAargau,
        'IsVacationZug': data.IsVacationZug,
        'IsVacationSchwyz': data.IsVacationSchwyz,
        'IsVacationSt_gallen': data.IsVacationSt_gallen,
        'IsVacationSchaffhausen': data.IsVacationSchaffhausen,
        'IsVacationThurgau': data.IsVacationThurgau,
        'Weekday': data.Weekday,
        'IsWeekend': data.IsWeekend
    }])

    # Make the prediction
    prediction = model.predict(input_df)
    return {"prediction": prediction[0]}
