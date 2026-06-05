from solution import search

# Test examples from docstring
assert search([4, 1, 2, 2, 3, 1]) == 2
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
assert search([5, 5, 4, 4, 4]) == -1

# Edge cases
assert search([1]) == 1
assert search([2]) == -1
assert search([1, 1, 1, 1, 1]) == 1
assert search([2, 2]) == 2
assert search([2, 2, 3, 3, 3]) == 3
assert search([1, 2, 3, 4, 5]) == 1
assert search([3, 3, 3, 3]) == 3
assert search([10, 10, 10, 10, 10]) == -1
