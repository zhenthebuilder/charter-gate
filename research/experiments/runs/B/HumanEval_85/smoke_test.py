from solution import add

# Test from docstring
assert add([4, 2, 6, 7]) == 2

# All odd elements at odd indices
assert add([1, 3, 5, 7]) == 0

# All even elements at odd indices
assert add([1, 2, 3, 4]) == 6

# Single element (no odd indices)
assert add([2]) == 0

# Two elements
assert add([2, 4]) == 4

# Single odd element at index 1
assert add([1, 1]) == 0

# Longer list: indices 1, 3, 5 have [5, 3, 8], only 8 is even
assert add([10, 5, 20, 3, 30, 8]) == 8

# Negative even numbers at odd indices
assert add([1, -2, 3, -4]) == -6
