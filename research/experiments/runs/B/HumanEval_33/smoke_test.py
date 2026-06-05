from solution import sort_third

# Examples from docstring
assert sort_third([1, 2, 3]) == [1, 2, 3]
assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

# Edge cases
assert sort_third([]) == []
assert sort_third([5]) == [5]
assert sort_third([5, 2]) == [5, 2]
assert sort_third([5, 2, 3]) == [5, 2, 3]
assert sort_third([5, 2, 3, 2]) == [2, 2, 3, 5]
assert sort_third([9, 1, 2, 6, 4, 5, 3, 7, 8]) == [3, 1, 2, 6, 4, 5, 9, 7, 8]
assert sort_third([-5, 1, 2, -3]) == [-5, 1, 2, -3]
assert sort_third([-3, 1, 2, -5]) == [-5, 1, 2, -3]
