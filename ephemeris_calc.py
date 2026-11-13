from skyfield.api import load
SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", 
         "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

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
    return float(lon.degrees)

def zodiac_sign(longitude):
    lon = longitude % 360
    sign_position = int(lon // 30)
    sign_degree = lon % 30

    sign_dict = {"sign" : SIGNS[sign_position], "degree": sign_degree}
    return sign_dict
