from ephemeris_calc import load_data, ecliptic_longitude, zodiac_sign
ts, eph = load_data()
t = ts.now()
t_test = ts.utc(2026, 10, 18, 12)
sun_test = ts.utc(2026, 12, 21, 12)
sun_lon = ecliptic_longitude(eph, t_test, "sun")
result = zodiac_sign(sun_lon)

print(t)
print(t.utc_iso())
print(t.utc_datetime())
print(ecliptic_longitude(eph, t_test, "moon"))
print(ecliptic_longitude(eph, sun_test, "sun"))
print(result)