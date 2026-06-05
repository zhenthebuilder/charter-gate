from solution import monotonic

# Examples from docstring
assert monotonic([1, 2, 4, 20]) == True
assert monotonic([1, 20, 4, 10]) == False
assert monotonic([4, 1, 0, -10]) == True

# Edge cases
assert monotonic([]) == True
assert monotonic([1]) == True
assert monotonic([1, 2]) == True
assert monotonic([2, 1]) == True

# Non-monotonic
assert monotonic([1, 3, 2]) == False
assert monotonic([3, 1, 2]) == False

# With equal consecutive elements
assert monotonic([1, 1, 2, 3]) == True
assert monotonic([3, 2, 2, 1]) == True
assert monotonic([1, 1, 1]) == True

# With negative numbers
assert monotonic([-4, -2, -1]) == True
assert monotonic([-1, -2, -4]) == True
