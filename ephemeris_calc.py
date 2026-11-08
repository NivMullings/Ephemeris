from skyfield.api import load

def load_data():
    ts = load.timescale()
    eph = load("de421.bsp")
    return ts, eph


def ecliptic_longitude(eph,t,body_name):
    earth = eph["earth"]
    body = eph[body_name]
    earth_time = earth.at(t)
    obs_loc = earth_time.observe(body)
    app_loc = obs_loc.apparent()
    lat,lon,dist = app_loc.ecliptic_latlon(epoch="date")
    return lon.degrees
