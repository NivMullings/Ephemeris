from ephemeris_calc import load_data, ecliptic_longitude
ts, eph = load_data()
t = ts.now()
t_test = ts.utc(2026, 10, 18, 12)
sun_test = ts.utc(2026, 12, 21, 12)

print(t)
print(t.utc_iso())
print(t.utc_datetime())
print(ecliptic_longitude(eph, t_test, "sun"))
print(ecliptic_longitude(eph, t_test, "moon"))
print(ecliptic_longitude(eph, t_test, "mercury"))
print(ecliptic_longitude(eph, t_test, "mars"))
print(ecliptic_longitude(eph, sun_test, "sun"))