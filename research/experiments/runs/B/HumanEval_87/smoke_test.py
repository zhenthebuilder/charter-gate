from solution import get_row

# Example 1
result = get_row([
    [1,2,3,4,5,6],
    [1,2,3,4,1,6],
    [1,2,3,4,5,1]
], 1)
assert result == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

# Example 2
result = get_row([], 1)
assert result == []

# Example 3
result = get_row([[], [1], [1, 2, 3]], 3)
assert result == [(2, 2)]

# Extra: single element
result = get_row([[5]], 5)
assert result == [(0, 0)]

# Extra: element not found
result = get_row([[1, 2, 3], [4, 5, 6]], 7)
assert result == []

# Extra: multiple in single row (descending)
result = get_row([[1, 1, 1]], 1)
assert result == [(0, 2), (0, 1), (0, 0)]

# Extra: multiple rows with different lengths
result = get_row([[2, 2], [2, 2, 2]], 2)
assert result == [(0, 1), (0, 0), (1, 2), (1, 1), (1, 0)]
