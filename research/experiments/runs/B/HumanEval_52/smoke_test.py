from solution import below_threshold

# Test examples from docstring
assert below_threshold([1, 2, 4, 10], 100) == True
assert below_threshold([1, 20, 4, 10], 5) == False

# Additional test cases
assert below_threshold([], 100) == True  # empty list
assert below_threshold([1], 2) == True  # single element below
assert below_threshold([5], 5) == False  # element equal to threshold (not below)
assert below_threshold([10], 5) == False  # single element above
assert below_threshold([-1, -2, -3], 0) == True  # negative numbers below
assert below_threshold([0, 1, 2], 3) == True  # all below threshold
assert below_threshold([3, 4, 5], 3) == False  # element at threshold fails
