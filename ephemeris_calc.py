from skyfield.api import load

def load_data():
    ts = load.timescale()
    eph = load("de421.bsp")
    return ts, eph

