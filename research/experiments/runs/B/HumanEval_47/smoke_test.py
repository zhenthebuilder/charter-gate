from solution import median

# Test cases from docstring
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Additional test cases
assert median([5]) == 5
assert median([1, 2]) == 1.5
assert median([1, 2, 3, 4]) == 3.5
assert median([1, 2, 3, 4, 5, 6, 7]) == 4
assert median([10, 20, 30]) == 20
assert median([-5, -3, -1, 0, 1]) == -1
