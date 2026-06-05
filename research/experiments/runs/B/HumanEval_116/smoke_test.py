from solution import sort_array

# Test 1: Basic case with various ones counts
result = sort_array([1, 5, 2, 3, 4])
# 1→1one, 5→2ones, 2→1one, 3→2ones, 4→1one
# Groups: 1one:[1,2,4], 2ones:[3,5]
assert result == [1, 2, 4, 3, 5], f"Expected [1, 2, 4, 3, 5], got {result}"

# Test 2: With zero
result = sort_array([1, 0, 2, 3, 4])
# 0→0ones, 1→1one, 2→1one, 3→2ones, 4→1one
# Groups: 0ones:[0], 1one:[1,2,4], 2ones:[3]
assert result == [0, 1, 2, 4, 3], f"Expected [0, 1, 2, 4, 3], got {result}"

# Test 3: Negative numbers
result = sort_array([-2, -3, -4, -5, -6])
# -2→1one, -3→2ones, -4→1one, -5→2ones, -6→2ones
# Groups: 1one:[-4,-2], 2ones:[-6,-5,-3]
assert result == [-4, -2, -6, -5, -3], f"Expected [-4, -2, -6, -5, -3], got {result}"

# Test 4: All same ones count - should sort by value
result = sort_array([7, 11, 13, 14])
# All have 3 ones: 7→111, 11→1011, 13→1101, 14→1110
assert result == [7, 11, 13, 14], f"Expected [7, 11, 13, 14], got {result}"

# Test 5: Edge case - single element
assert sort_array([5]) == [5]

# Test 6: Duplicates
result = sort_array([1, 1, 2, 2, 3])
assert result == [1, 1, 2, 2, 3]
