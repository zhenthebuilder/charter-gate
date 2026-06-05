from solution import sum_product

# Test cases from docstring
assert sum_product([]) == (0, 1)
assert sum_product([1, 2, 3, 4]) == (10, 24)

# Additional test cases
assert sum_product([1]) == (1, 1)
assert sum_product([2, 3]) == (5, 6)
assert sum_product([0]) == (0, 0)
assert sum_product([-1, -2, -3]) == (-6, -6)
assert sum_product([-1, 2]) == (1, -2)
