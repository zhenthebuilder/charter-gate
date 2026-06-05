from solution import string_sequence

# Test cases from docstring
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'

# Additional test cases
assert string_sequence(1) == '0 1'
assert string_sequence(3) == '0 1 2 3'
assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
