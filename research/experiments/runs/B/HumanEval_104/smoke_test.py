from solution import unique_digits

# Docstring examples
assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
assert unique_digits([152, 323, 1422, 10]) == []

# Edge cases
assert unique_digits([]) == []
assert unique_digits([7]) == [7]
assert unique_digits([2]) == []
assert unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
assert unique_digits([2, 4, 6, 8, 0]) == []
assert unique_digits([135, 246, 579]) == [135, 579]
assert unique_digits([135, 13, 1]) == [1, 13, 135]
assert unique_digits([11, 13, 15, 17, 19, 20]) == [11, 13, 15, 17, 19]
assert unique_digits([111, 113, 112]) == [111, 113]
