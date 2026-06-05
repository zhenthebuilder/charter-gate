from solution import derivative

# Test cases from docstring
assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
assert derivative([1, 2, 3]) == [2, 6]

# Additional test cases
assert derivative([]) == []  # Empty polynomial
assert derivative([5]) == []  # Constant polynomial
assert derivative([3, 4]) == [4]  # Linear polynomial
assert derivative([1, 2, 3, 4]) == [2, 6, 12]  # Cubic polynomial
assert derivative([0, 1, 2]) == [1, 4]  # Polynomial with zero constant term
