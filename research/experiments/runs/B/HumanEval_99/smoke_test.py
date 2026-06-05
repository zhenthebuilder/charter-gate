from solution import closest_integer

# Examples from docstring
assert closest_integer("10") == 10
assert closest_integer("15.3") == 15

# Rounding away from zero (equidistant cases)
assert closest_integer("14.5") == 15
assert closest_integer("-14.5") == -15

# Additional cases
assert closest_integer("10.1") == 10
assert closest_integer("10.6") == 11
assert closest_integer("15.4") == 15
assert closest_integer("15.5") == 16
assert closest_integer("-15.3") == -15
assert closest_integer("-15.5") == -16
assert closest_integer("-10.1") == -10
assert closest_integer("-10.6") == -11
assert closest_integer("0") == 0
assert closest_integer("0.5") == 1
assert closest_integer("-0.5") == -1
