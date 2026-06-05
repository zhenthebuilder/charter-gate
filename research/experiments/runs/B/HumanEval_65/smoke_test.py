from solution import circular_shift

# Examples from docstring
assert circular_shift(12, 1) == "21"
assert circular_shift(12, 2) == "12"

# Additional test cases
assert circular_shift(123, 1) == "312"
assert circular_shift(123, 2) == "231"
assert circular_shift(123, 3) == "123"
assert circular_shift(123, 4) == "321"
assert circular_shift(1234, 2) == "3412"
assert circular_shift(12345, 2) == "45123"
assert circular_shift(5, 1) == "5"
assert circular_shift(5, 2) == "5"
assert circular_shift(0, 1) == "0"
