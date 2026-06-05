from solution import specialFilter

# Test examples from docstring
assert specialFilter([15, -73, 14, -15]) == 1
assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

# Edge cases
assert specialFilter([]) == 0
assert specialFilter([10]) == 0
assert specialFilter([11]) == 1
assert specialFilter([9]) == 0

# Single qualifying numbers
assert specialFilter([13]) == 1
assert specialFilter([31]) == 1
assert specialFilter([111]) == 1
assert specialFilter([19]) == 1
assert specialFilter([91]) == 1

# Non-qualifying numbers (even first or last digit)
assert specialFilter([21]) == 0
assert specialFilter([12]) == 0
assert specialFilter([23]) == 0

# Multiple qualifying numbers
assert specialFilter([13, 31, 51, 71, 91]) == 5

# Mixed with non-qualifying
assert specialFilter([13, 21, 31, 42, 51]) == 3

# Negative numbers
assert specialFilter([-15]) == 0
assert specialFilter([-33]) == 0
