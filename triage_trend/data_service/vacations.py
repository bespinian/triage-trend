from datetime import datetime, timedelta


def is_date_in_range(date_str, start_str, end_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    start = datetime.strptime(start_str, "%d.%m")
    end = datetime.strptime(end_str, "%d.%m")
    # Adjust year for the comparison
    start = start.replace(year=date.year)
    end = end.replace(year=date.year)
    return start <= date <= end


def get_vacation_data(date_str):
    vacation_data = {
        "Zurich": [
            ("22.04", "04.05"),
            ("15.07", "17.08"),
            ("07.10", "19.10"),
            ("23.12", "04.01"),
        ],
        "Bern": [
            ("06.04", "21.04"),
            ("06.07", "11.08"),
            ("21.09", "13.10"),
            ("21.12", "05.01"),
        ],
        "Luzern": [
            ("28.03", "14.04"),
            ("03.02", "18.02"),
            ("06.07", "18.08"),
            ("28.09", "13.10"),
            ("21.12", "05.01"),
        ],
        "Uri": [("27.04", "12.05"), ("02.03", "10.03"), ("06.07", "18.08")],
        "Schwyz": [
            ("29.04", "10.05"),
            ("26.02", "01.03"),
            ("30.09", "11.10"),
            ("25.12", "06.01"),
        ],
        "Zug": [
            ("13.04", "28.04"),
            ("03.02", "18.02"),
            ("06.07", "18.08"),
            ("05.10", "20.10"),
            ("21.12", "05.01"),
        ],
        "Schaffhausen": [
            ("13.04", "28.04"),
            ("27.01", "11.02"),
            ("06.07", "11.08"),
            ("28.09", "20.10"),
            ("24.12", "05.01"),
        ],
        "St_gallen": [
            ("07.04", "21.04"),
            ("07.07", "11.08"),
            ("29.09", "20.10"),
            ("22.12", "05.01"),
        ],
        "Aargau": [
            ("08.04", "19.04"),
            ("22.07", "09.08"),
            ("30.09", "11.10"),
            ("23.12", "03.01"),
        ],
        "Thurgau": [
            ("29.03", "14.04"),
            ("29.01", "04.02"),
            ("08.07", "11.08"),
            ("07.10", "20.10"),
            ("23.12", "05.01"),
        ],
    }

    vacations = {}
    for canton, periods in vacation_data.items():
        in_vacation = any(
            is_date_in_range(date_str, start, end) for start, end in periods
        )
        first_week_of_holiday = any(
            is_date_in_range(
                date_str,
                start,
                (
                    datetime.strptime(start, "%d.%m") + timedelta(days=7)
                ).strftime("%d.%m"),
            )
            for start, end in periods
        )
        week_after_holiday = any(
            is_date_in_range(
                date_str,
                (datetime.strptime(end, "%d.%m") + timedelta(days=1)).strftime(
                    "%d.%m"
                ),
                (datetime.strptime(end, "%d.%m") + timedelta(days=7)).strftime(
                    "%d.%m"
                ),
            )
            for start, end in periods
        )

        # Ensure all keys match the model's expected format
        canton_key = canton.replace(" ", "_")
        vacations[f"IsVacation{canton_key}"] = int(in_vacation)
        vacations[f"{canton_key}_First_Week_of_Holiday"] = int(
            first_week_of_holiday
        )
        vacations[f"{canton_key}_Week_After_Holiday"] = int(week_after_holiday)

    return vacations
