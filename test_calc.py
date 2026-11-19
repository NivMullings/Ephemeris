from ephemeris_calc import zodiac_sign, signed_difference, load_data, is_retrograde
ts, eph = load_data()


deg_zero = zodiac_sign(0)
assert deg_zero["sign"] == "Aries"
assert abs(deg_zero["degree"] - 0) < 0.0001

deg_zero = zodiac_sign(29.99)
assert deg_zero["sign"] == "Aries"
assert abs(deg_zero["degree"] - 29.99) < 0.0001

deg_zero = zodiac_sign(30)
assert deg_zero["sign"] == "Taurus"
assert abs(deg_zero["degree"] - 0) < 0.0001

deg_zero = zodiac_sign(359.99)
assert deg_zero["sign"] == "Pisces"
assert abs(deg_zero["degree"] - 29.99) < 0.0001

deg_zero = zodiac_sign(360)
assert deg_zero["sign"] == "Aries"
assert abs(deg_zero["degree"] - 0) < 0.0001

deg_zero = zodiac_sign(-10)
assert deg_zero["sign"] == "Pisces"
assert abs(deg_zero["degree"] - 20) < 0.0001

deg_zero = zodiac_sign(725)
assert deg_zero["sign"] == "Aries"
assert abs(deg_zero["degree"] - 5) < 0.0001

print("All sign name tests have passed")


assert signed_difference(359, 1) == 2
assert signed_difference(1, 359) == -2
assert signed_difference(10, 20) == 10
assert signed_difference(20, 10) == -10
assert signed_difference(350, 10) == 20
assert signed_difference(10, 350) == -20
assert signed_difference(90, 90) == 0

print("All angle tool tests have passed")


assert is_retrograde(eph, ts.utc(2026, 1, 15, 12), "mercury") == False
assert is_retrograde(eph, ts.utc(2026, 3, 5, 12), "mercury") == True
assert is_retrograde(eph, ts.utc(2026, 5, 15, 12), "mercury") == False
assert is_retrograde(eph, ts.utc(2026, 7, 10, 12), "mercury") == True
assert is_retrograde(eph, ts.utc(2026, 9, 1, 12), "mercury") == False
assert is_retrograde(eph, ts.utc(2026, 11, 1, 12), "mercury") == True
assert is_retrograde(eph, ts.utc(2026, 12, 15, 12), "mercury") == False

print("All Mercury retrograde tests have passed")