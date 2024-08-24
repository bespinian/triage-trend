from datetime import datetime
import ephem

def get_moon_phase(date_obj):
    moon = ephem.Moon(date_obj)
    return moon.phase

def get_data(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    weekday = date_obj.weekday()
    is_weekend = 1 if weekday >= 5 else 0
    moon_phase = get_moon_phase(date_obj)

    raw_data = {
        "Average_Temperature": 20.0,
        "Max_Temperature": 25.0,
        "Total_Rain_Duration": 2.0,
        "Average_Pressure": 1010.0,
        "Average_Global_Radiation": 220.0,
        "Cloudiness": 0.3,
        "Moon Phase (%)": moon_phase,
        "IsVacationAargau": 0,
        "IsVacationZug": 0,
        "IsVacationSchwyz": 0,
        "IsVacationSt_gallen": 0,
        "IsVacationSchaffhausen": 0,
        "IsVacationThurgau": 0,
        "IsVacationZurich": 0,
        "Weekday": weekday,
        "IsWeekend": is_weekend,
        "Aargau_Week_After_Holiday": 0,
        "Aargau_First_Week_of_Holiday": 0,
        "Zug_Week_After_Holiday": 0,
        "Zug_First_Week_of_Holiday": 0,
        "Schwyz_Week_After_Holiday": 0,
        "Schwyz_First_Week_of_Holiday": 0,
        "St_gallen_Week_After_Holiday": 0,
        "St_gallen_First_Week_of_Holiday": 0,
        "Schaffhausen_Week_After_Holiday": 0,
        "Schaffhausen_First_Week_of_Holiday": 0,
        "Thurgau_Week_After_Holiday": 0,
        "Thurgau_First_Week_of_Holiday": 0,
        "Zurich_Week_After_Holiday": 0,
        "Zurich_First_Week_of_Holiday": 0,
        "Average_Temperature_5day_mean": 19.5,
        "Max_Temperature_5day_mean": 24.5,
        "Total_Rain_Duration_5day_mean": 1.8,
        "Average_Pressure_5day_mean": 1012.0,
        "Average_Global_Radiation_5day_mean": 215.0,
        "Cloudiness_5day_mean": 0.25,
        "publicHolidayAargau": 0,
        "publicHolidayZug": 0,
        "publicHolidaySchwyz": 0,
        "publicHolidayStGallen": 0,
        "publicHolidayThurgau": 0,
        "publicHolidaySchaffhausen": 0,
        "publicHolidayZurich": 0,
    }

    return raw_data
