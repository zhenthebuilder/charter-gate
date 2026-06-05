from solution import prod_signs

# From docstring examples
assert prod_signs([1, 2, 2, -4]) == -9
assert prod_signs([0, 1]) == 0
assert prod_signs([]) is None

# Additional cases from specification
assert prod_signs([1, 2, 3]) == 6
assert prod_signs([-1, -2, -3, -4]) == 10  # even negatives, sign product = 1
assert prod_signs([-1, -2, -3]) == -6  # odd negatives, sign product = -1
assert prod_signs([5]) == 5
assert prod_signs([-5]) == -5
assert prod_signs([0]) == 0
assert prod_signs([1, 2, 0, 3]) == 0  # zero makes product 0
assert prod_signs([0, 0, 0]) == 0
assert prod_signs([-1, -1, 2, 3]) == 7  # even negatives (2), sum = 7, product = 1
