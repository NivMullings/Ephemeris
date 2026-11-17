from ephemeris_calc import load_data, ecliptic_longitude, zodiac_sign, get_positions
ts, eph = load_data()
t = ts.now()
t_test = ts.utc(2026, 10, 18, 12)
sun_test = ts.utc(2026, 12, 21, 12)
sun_lon = ecliptic_longitude(eph, t_test, "sun")
result = zodiac_sign(sun_lon)

pos_list = get_positions(t_test, eph)

for planet in pos_list:
    name = planet["name"]
    longitude = planet["longitude"]
    sign = planet["sign"]
    degree = planet["degree"]
    print(f"{name:<8}, {longitude:7.2f}, {sign:<10}, {degree:.2f}")

"""
print(t)
print(t.utc_iso())
print(t.utc_datetime())
print(ecliptic_longitude(eph, t_test, "moon"))
print(ecliptic_longitude(eph, sun_test, "sun"))
print(result)
"""

