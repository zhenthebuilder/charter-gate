from solution import is_simple_power

# Examples from docstring
assert is_simple_power(1, 4) == True
assert is_simple_power(2, 2) == True
assert is_simple_power(8, 2) == True
assert is_simple_power(3, 2) == False
assert is_simple_power(3, 1) == False
assert is_simple_power(5, 3) == False

# Additional powers
assert is_simple_power(1, 1) == True
assert is_simple_power(4, 2) == True
assert is_simple_power(27, 3) == True
assert is_simple_power(16, 2) == True
assert is_simple_power(1, 100) == True

# n = 0 cases
assert is_simple_power(1, 0) == True
assert is_simple_power(0, 0) == True
assert is_simple_power(2, 0) == False

# n = -1 cases
assert is_simple_power(1, -1) == True
assert is_simple_power(-1, -1) == True
assert is_simple_power(2, -1) == False

# Negative base cases
assert is_simple_power(-2, -2) == True
assert is_simple_power(4, -2) == True
assert is_simple_power(-8, -2) == True

# Negative x with positive base
assert is_simple_power(-8, 2) == False
