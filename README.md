# triage-trend

Our awesome BärnHäckt project for the Clienia Schlössli challenge

## Install and run backend

```
poetry install
poetry run python train.py
poetry run uvicorn triage_trend.main:app --reload
```

The service can then be queried like this:

```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{
    "Average_Temperature": 15.0,
    "Max_Temperature": 20.0,
    "Total_Rain_Duration": 5.0,
    "Average_Pressure": 1013.0,
    "Average_Global_Radiation": 200.0,
    "Cloudiness": 0.5,
    "Moon_Phase": 50.0,
    "IsVacationAargau": 0,
    "IsVacationZug": 0,
    "IsVacationSchwyz": 0,
    "IsVacationSt_gallen": 0,
    "IsVacationSchaffhausen": 0,
    "IsVacationThurgau": 0,
    "Weekday": 3,
    "IsWeekend": 0
}'
```

## Format python code

```bash
ruff check . --fix
ruff format
```

## Setup NixOS

```bash
echo "use nix" > .envrc

direnv allow
```

## Data sources

- [Weather data](https://data.stadt-zuerich.ch/dataset/ugz_meteodaten_tagesmittelwerte)

## Feature engineering ideas

- Week after holidays
- First week of holidays
- Mean week weather data
