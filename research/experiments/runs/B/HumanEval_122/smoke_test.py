from solution import add_elements

# Test from docstring example
assert add_elements([111,21,3,4000,5,6,7,8,9], 4) == 24

# All elements within limit
assert add_elements([1,2,3,4,5], 5) == 15

# No elements within limit in first k
assert add_elements([111, 222, 333, 1, 2], 3) == 0

# Negative numbers within limit
assert add_elements([-1, -99, -100, 50], 4) == -50

# Single element within limit
assert add_elements([5, 100], 1) == 5

# Single large element
assert add_elements([100], 1) == 0

# Boundary: 99 and -99 are valid, 100 and -100 are not
assert add_elements([99, -99, 100, -100], 4) == 0

# All large numbers
assert add_elements([1000, 2000, 3000], 3) == 0

# Mixed with zero (within limit)
assert add_elements([0, 100, 1, 200], 4) == 1

# k is less than array length
assert add_elements([10, 20, 1000, 30], 2) == 30
