# triage-trend

Our awesome BärnHäckt project for the Clienia Schlössli challenge

## Install and run backend

```
poetry install
poetry run python train.py
poetry run uvicorn triage_trend.main:app --reload
```

The service can then be queried like this:

````bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{
    "date": "2024-08-24"
}'
`
## Install and run the frontend
```bash
cd ./triage-trend-ui
npm install
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
````

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
