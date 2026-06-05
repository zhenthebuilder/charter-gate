from solution import sort_even

# Test docstring examples
assert sort_even([1, 2, 3]) == [1, 2, 3]
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

# Edge cases
assert sort_even([]) == []
assert sort_even([1]) == [1]
assert sort_even([2, 1]) == [2, 1]

# Additional cases
assert sort_even([3, 2, 1]) == [1, 2, 3]
assert sort_even([4, 8, 3, 7, 2, 6]) == [2, 8, 3, 7, 4, 6]
assert sort_even([10, 5, 9, 3, 8, 1]) == [8, 5, 9, 3, 10, 1]
