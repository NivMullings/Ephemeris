from ephemeris_calc import load_data, ecliptic_longitude, zodiac_sign, get_positions, BODIES, is_retrograde, find_aspects
ts, eph = load_data()
t = ts.now()
t_test = ts.utc(2026, 10, 18, 12)
sun_test = ts.utc(2026, 12, 21, 12)
sun_lon = ecliptic_longitude(eph, t_test, "sun")
result = zodiac_sign(sun_lon)

# Positions list: where planets are by name/longitude/sign/degree
pos_list = get_positions(t_test, eph)

# Expected aspects check
aspects = find_aspects(pos_list) 
for aspect in aspects:
    body_1 = aspect["body1"]
    body_2 = aspect["body2"]
    aspect_name = aspect["aspect"]
    separation = aspect["separation"]
    orb = aspect["orb"]
    print(f"{body_1:<8}{body_2:<8}{aspect_name:<12}{separation:8.2f}{orb:6.2f}")

"""
# Planet position check
for planet in pos_list:
    name = planet["name"]
    longitude = planet["longitude"]
    sign = planet["sign"]
    degree = planet["degree"]
    print(f"{name:<8}{longitude:7.2f}{sign:<10} {degree:.2f}")
"""
"""
# Retrograde check
for display_name, eph_name in BODIES.items():
    ret_check = is_retrograde(eph, t_test, eph_name)
    print(display_name, ret_check)
"""
"""
print(t)
print(t.utc_iso())
print(t.utc_datetime())

# Longitude tests
print(ecliptic_longitude(eph, t_test, "moon"))
print(ecliptic_longitude(eph, sun_test, "sun"))
print(result)
"""

