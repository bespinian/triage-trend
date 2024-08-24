from datetime import datetime

from triage_trend.data_service.moon_phase import get_moon_phase
from triage_trend.data_service.public_holidays import get_public_holidays
from triage_trend.data_service.vacations import get_vacation_data
from triage_trend.data_service.weather_forecast import get_weather_forecast


def get_data(date_str):
    forecast_data = get_weather_forecast()
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    weekday = date_obj.weekday()
    is_weekend = 1 if weekday >= 5 else 0
    moon_phase = get_moon_phase(date_obj)
    holidays = get_public_holidays(date_str)
    vacations = get_vacation_data(date_str)
    forecast = forecast_data.get(date_str, forecast_data[date_str])

    raw_data = {
        "Average_Temperature": forecast["Avg_Temp"],
        "Max_Temperature": forecast["Max_Temp"],
        "Total_Rain_Duration": forecast["Rain_Duration"],
        "Average_Pressure": forecast["Pressure"],
        "Average_Global_Radiation": forecast["Radiation"],
        "Cloudiness": forecast["Cloudiness"],
        "Moon Phase (%)": moon_phase,
        **vacations,
        "Weekday": weekday,
        "IsWeekend": is_weekend,
        "Average_Temperature_5day_mean": (forecast["Avg_Temp"] + 19.0) / 2,
        "Max_Temperature_5day_mean": (forecast["Max_Temp"] + 24.0) / 2,
        "Total_Rain_Duration_5day_mean": (forecast["Rain_Duration"] + 1.8) / 2,
        "Average_Pressure_5day_mean": (forecast["Pressure"] + 1012.0) / 2,
        "Average_Global_Radiation_5day_mean": (forecast["Radiation"] + 215.0)
        / 2,
        "Cloudiness_5day_mean": (forecast["Cloudiness"] + 0.25) / 2,
        **holidays,
    }

    return raw_data
