from solution import change_base

# Test cases from docstring
assert change_base(8, 3) == '22'
assert change_base(8, 2) == '1000'
assert change_base(7, 2) == '111'

# Additional test cases
assert change_base(0, 2) == '0'
assert change_base(1, 2) == '1'
assert change_base(15, 2) == '1111'
assert change_base(27, 3) == '1000'
assert change_base(100, 10) == '100'
assert change_base(5, 2) == '101'
assert change_base(10, 3) == '101'
