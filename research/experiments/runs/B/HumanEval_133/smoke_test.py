from solution import sum_squares

# Examples from docstring
assert sum_squares([1, 2, 3]) == 14
assert sum_squares([1, 4, 9]) == 98
assert sum_squares([1, 3, 5, 7]) == 84
assert sum_squares([1.4, 4.2, 0]) == 29
assert sum_squares([-2.4, 1, 1]) == 6

# Additional test cases
assert sum_squares([]) == 0
assert sum_squares([0]) == 0
assert sum_squares([0.5]) == 1
assert sum_squares([-1.5]) == 1
assert sum_squares([2.1, 2.9]) == 18
