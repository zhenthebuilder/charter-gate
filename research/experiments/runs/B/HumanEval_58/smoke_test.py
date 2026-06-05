from solution import common

# Test cases from docstring
assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
assert common([5, 3, 2, 8], [3, 2]) == [2, 3]

# Additional test cases
assert common([1, 2, 3], [4, 5, 6]) == []
assert common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
assert common([1], [1]) == [1]
assert common([], [1, 2, 3]) == []
assert common([1, 2, 3], []) == []
assert common([1, 1, 1], [1, 1, 1]) == [1]
assert common([3, 1, 2], [2, 1, 3]) == [1, 2, 3]
