import ephem


def get_moon_phase(date_obj):
    moon = ephem.Moon(date_obj)
    return moon.phase
