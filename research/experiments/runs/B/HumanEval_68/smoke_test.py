from solution import pluck

# Example 1
assert pluck([4, 2, 3]) == [2, 1]

# Example 2
assert pluck([1, 2, 3]) == [2, 1]

# Example 3
assert pluck([]) == []

# Example 4
assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

# No even values
assert pluck([1, 3, 5, 7]) == []

# Single even value
assert pluck([1, 4, 3]) == [4, 1]

# Multiple same even values
assert pluck([2, 2, 2]) == [2, 0]

# Zero at start
assert pluck([0, 1, 2]) == [0, 0]

# Single element (even)
assert pluck([6]) == [6, 0]

# Single element (odd)
assert pluck([5]) == []
