from solution import filter_integers

# Test cases from docstring
assert filter_integers(['a', 3.14, 5]) == [5]
assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]

# Additional test cases
assert filter_integers([]) == []
assert filter_integers([1, 2, 3]) == [1, 2, 3]
assert filter_integers([-1, -2, 'x']) == [-1, -2]
assert filter_integers([0, 1]) == [0, 1]
assert filter_integers([999999999, 1.5]) == [999999999]
assert filter_integers([10, 20.5, -5]) == [10, -5]
