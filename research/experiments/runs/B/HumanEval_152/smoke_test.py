from solution import compare

# Test case 1 from docstring
assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]

# Test case 2 from docstring
assert compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) == [4,4,1,0,0,6]

# Empty arrays
assert compare([], []) == []

# All correct guesses
assert compare([5, 10, -3], [5, 10, -3]) == [0, 0, 0]

# All incorrect guesses
assert compare([1, 2, 3], [0, 0, 0]) == [1, 2, 3]

# Negative numbers
assert compare([-5, -3, -1], [-2, -4, 0]) == [3, 1, 1]

# Single element
assert compare([10], [7]) == [3]
