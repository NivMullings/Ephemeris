from ephemeris_calc import zodiac_sign

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

print("All tests have passed")