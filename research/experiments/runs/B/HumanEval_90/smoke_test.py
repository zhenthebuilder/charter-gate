from solution import next_smallest

# From docstring
assert next_smallest([1, 2, 3, 4, 5]) == 2
assert next_smallest([5, 1, 4, 3, 2]) == 2
assert next_smallest([]) == None
assert next_smallest([1, 1]) == None

# Extra cases
assert next_smallest([1]) == None
assert next_smallest([2, 1]) == 2
assert next_smallest([1, 2, 1, 2]) == 2
assert next_smallest([3, 1, 2]) == 2
assert next_smallest([1, 1, 1]) == None
assert next_smallest([-5, -1, 0, 3]) == -1
