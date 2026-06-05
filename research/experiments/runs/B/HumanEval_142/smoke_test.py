from solution import sum_squares

# Test case 1 from docstring
assert sum_squares([1, 2, 3]) == 6

# Test case 2 from docstring
assert sum_squares([]) == 0

# Test case 3 from docstring
assert sum_squares([-1, -5, 2, -1, -5]) == -126

# Additional test: verify index 4 is cubed (multiple of 4, not multiple of 3)
assert sum_squares([0, 0, 0, 0, 2]) == 8  # index 4: 2^3 = 8

# Additional test: verify index 12 is squared (multiple of 3 takes precedence over multiple of 4)
assert sum_squares([0] * 12 + [2]) == 4  # index 12: 2^2 = 4 (squared, not cubed)

# Additional test: verify index 8 is cubed (multiple of 4, not of 3)
assert sum_squares([0] * 8 + [2]) == 8  # index 8: 2^3 = 8
