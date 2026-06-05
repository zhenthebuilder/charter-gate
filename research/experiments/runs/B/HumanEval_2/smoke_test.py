from solution import truncate_number

# Test from docstring
assert truncate_number(3.5) == 0.5

# Additional test cases
assert truncate_number(0.5) == 0.5
assert truncate_number(10.0) == 0.0
assert abs(truncate_number(5.1) - 0.1) < 1e-9
assert abs(truncate_number(2.999) - 0.999) < 1e-9
