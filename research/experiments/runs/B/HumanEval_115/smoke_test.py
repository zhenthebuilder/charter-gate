from solution import max_fill

# Example 1
assert max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6

# Example 2
assert max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5

# Example 3
assert max_fill([[0,0,0], [0,0,0]], 5) == 0

# Single well with exact capacity match
assert max_fill([[1]], 1) == 1

# Capacity larger than water
assert max_fill([[1]], 5) == 1

# Multiple units, capacity fits exactly
assert max_fill([[1,1,1]], 3) == 1

# Multiple units, needs rounding up
assert max_fill([[1,1,1]], 2) == 2

# Empty well
assert max_fill([[0]], 1) == 0
