from solution import compare_one

# Test cases from docstring
assert compare_one(1, 2.5) == 2.5
assert compare_one(1, "2,3") == "2,3"
assert compare_one("5,1", "6") == "6"
assert compare_one("1", 1) is None

# First argument larger
assert compare_one(5, 3) == 5
assert compare_one(5.0, 3) == 5.0
assert compare_one("5", 3) == "5"
assert compare_one("5,5", "3,3") == "5,5"

# Equal values (different types but same numeric value)
assert compare_one(3, 3) is None
assert compare_one(3.5, 3.5) is None
assert compare_one("1.5", 1.5) is None
assert compare_one("2,5", 2.5) is None
assert compare_one(1, "1") is None

# Mixed types
assert compare_one("10", 9) == "10"
assert compare_one(10, "9") == 10

# Negative numbers
assert compare_one(-5, -3) == -3
assert compare_one("-10", -5) == -5
