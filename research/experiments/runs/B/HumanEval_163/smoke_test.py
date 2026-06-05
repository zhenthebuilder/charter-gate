from solution import generate_integers

# Test cases from docstring
assert generate_integers(2, 8) == [2, 4, 6, 8]
assert generate_integers(8, 2) == [2, 4, 6, 8]
assert generate_integers(10, 14) == []

# Additional test cases
assert generate_integers(1, 9) == [2, 4, 6, 8]
assert generate_integers(1, 7) == [2, 4, 6]
assert generate_integers(5, 5) == []
assert generate_integers(4, 4) == [4]
assert generate_integers(2, 2) == [2]
assert generate_integers(3, 5) == [4]
assert generate_integers(1, 1) == []
assert generate_integers(6, 9) == [6, 8]
