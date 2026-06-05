from solution import sort_array

# Test cases from docstring
assert sort_array([]) == []
assert sort_array([5]) == [5]
assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]

# Additional test cases
# Two elements with odd sum (1+2=3)
assert sort_array([2, 1]) == [1, 2]

# Two elements with even sum (2+4=6)
assert sort_array([4, 2]) == [4, 2]

# Larger array with odd sum (1+9=10... wait, 10 is even)
# Larger array with odd sum (1+8=9)
assert sort_array([5, 3, 1, 4, 8]) == [1, 3, 4, 5, 8]

# Larger array with even sum (3+7=10)
assert sort_array([3, 1, 5, 2, 7]) == [7, 5, 3, 2, 1]

# Verify original array is not modified
original = [2, 4, 3, 0, 1, 5]
original_copy = original.copy()
sort_array(original)
assert original == original_copy
