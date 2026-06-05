from solution import intersection

# Examples from docstring
assert intersection((1, 2), (2, 3)) == "NO"
assert intersection((-1, 1), (0, 4)) == "NO"
assert intersection((-3, -1), (-5, 5)) == "YES"

# No intersection
assert intersection((1, 2), (3, 4)) == "NO"

# Prime lengths
assert intersection((1, 3), (2, 4)) == "NO"  # length = 1
assert intersection((1, 4), (1, 5)) == "YES"  # length = 3
assert intersection((1, 6), (1, 7)) == "YES"  # length = 5
assert intersection((1, 8), (1, 9)) == "YES"  # length = 7

# Non-prime lengths
assert intersection((1, 5), (1, 6)) == "NO"   # length = 4
assert intersection((1, 7), (1, 8)) == "NO"   # length = 6
assert intersection((1, 9), (1, 10)) == "NO"  # length = 8

# Negative numbers
assert intersection((-10, -5), (-7, 0)) == "YES"   # length = 2
assert intersection((-5, 5), (-3, 3)) == "NO"     # length = 6
