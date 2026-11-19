from skyfield.api import load

SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", 
         "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

BODIES = {"Sun":"sun", "Moon":"moon", "Mercury":"mercury", "Venus":"venus",
          "Mars":"mars", "Jupiter":"jupiter barycenter", "Saturn":"saturn barycenter", 
            "Uranus":"uranus barycenter", "Neptune":"neptune barycenter", "Pluto": "pluto barycenter"}

def load_data():
    ts = load.timescale()
    eph = load("de421.bsp")
    return ts, eph


def ecliptic_longitude(eph,t,body_name):
    # takes the ephemeris, a time, and a body's name and returns
    # that body's tropical ecliptic longitude in degrees
    # as a plain float from 0 to 360
    earth = eph["earth"]
    body = eph[body_name]
    earth_time = earth.at(t)
    obs_loc = earth_time.observe(body)
    app_loc = obs_loc.apparent()
    lat,lon,dist = app_loc.ecliptic_latlon(epoch="date")
    return float(lon.degrees)

def zodiac_sign(longitude):
    # takes any number of degrees and returns a dict with two keys:
    # "sign" (sign's name) and "degree" (how far into the sign 0-30)
    lon = longitude % 360
    sign_position = int(lon // 30)
    sign_degree = lon % 30

    sign_dict = {"sign" : SIGNS[sign_position], "degree": sign_degree}
    return sign_dict

def get_positions(t, eph):
    # returns a list of ten dicts, one per body, each with the keys "name", 
    # "longitude", "sign", and "degree", sorted by longitude
    result = []
    for display_name, eph_name in BODIES.items():
        body_lon = ecliptic_longitude(eph, t, eph_name)
        zodiac_dict = zodiac_sign(body_lon)
        body_dict = {"name": display_name, "longitude": body_lon, 
                     "sign": zodiac_dict["sign"], "degree": zodiac_dict["degree"]}
        result.append(body_dict)
    by_lon = sorted(result, key=lambda p: p["longitude"])
    return by_lon

def signed_difference(a, b):
    # how far you turn, in the shortest way, to get from angle a to angle b
    ret_angle = ((b - a) + 180) % 360 - 180
    return ret_angle

def is_retrograde(eph, t, body_name):
    # uses def signed_difference to return True or False
    if body_name == "sun" or body_name == "moon":
        return False
    lon_now = ecliptic_longitude(eph, t, body_name)
    lon_tmw = ecliptic_longitude(eph, t + 1, body_name)
    ret_diff = signed_difference(lon_now, lon_tmw)
    if ret_diff < 0:
        return True
    else:
        return False
