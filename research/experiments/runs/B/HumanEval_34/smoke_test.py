from solution import unique

# Test from docstring
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Edge cases
assert unique([]) == []
assert unique([1]) == [1]
assert unique([1, 1, 1]) == [1]
assert unique([3, 2, 1]) == [1, 2, 3]
assert unique([3, -1, 2, -1]) == [-1, 2, 3]
assert unique([1, 2, 3, 1, 2]) == [1, 2, 3]
