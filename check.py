from ephemeris_calc import load_data
ts, eph = load_data()
t = ts.now()
print(t)
print(t.utc_iso())
print(t.utc_datetime())
