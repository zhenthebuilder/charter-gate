from solution import minSubArraySum

# Examples from docstring
assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
assert minSubArraySum([-1, -2, -3]) == -6

# Single element
assert minSubArraySum([5]) == 5
assert minSubArraySum([-5]) == -5

# All positive numbers - minimum is the smallest single element
assert minSubArraySum([1, 2, 3, 4]) == 1

# All negative numbers - minimum is the sum of all
assert minSubArraySum([-5, -2, -3]) == -10

# Mixed with zeros
assert minSubArraySum([1, 0, -1, 2]) == -1

# Minimum is a sub-array in the middle
assert minSubArraySum([5, -3, -2, 1]) == -5

print("All tests passed!")
