from solution import is_sorted

# Test cases from the docstring
assert is_sorted([5]) == True
assert is_sorted([1, 2, 3, 4, 5]) == True
assert is_sorted([1, 3, 2, 4, 5]) == False
assert is_sorted([1, 2, 3, 4, 5, 6]) == True
assert is_sorted([1, 2, 3, 4, 5, 6, 7]) == True
assert is_sorted([1, 3, 2, 4, 5, 6, 7]) == False
assert is_sorted([1, 2, 2, 3, 3, 4]) == True
assert is_sorted([1, 2, 2, 2, 3, 4]) == False

# Additional cases
assert is_sorted([]) == True
assert is_sorted([1, 2]) == True
assert is_sorted([2, 1]) == False
assert is_sorted([1, 1]) == True
assert is_sorted([1, 1, 1]) == False
assert is_sorted([1, 1, 2, 2, 3, 3]) == True
assert is_sorted([1, 2, 2, 1]) == False
