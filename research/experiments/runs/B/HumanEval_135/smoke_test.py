from solution import can_arrange

# From docstring examples
assert can_arrange([1,2,4,3,5]) == 3
assert can_arrange([1,2,3]) == -1

# Additional test cases from specification
assert can_arrange([5,4,3,2,1]) == 4  # Strictly decreasing array
assert can_arrange([1]) == -1  # Single element
assert can_arrange([2,1]) == 1  # Simple violation
assert can_arrange([1,3,2,4]) == 2  # Violation in middle
assert can_arrange([1,5,2,3,4]) == 2  # Only one violation, return largest index
assert can_arrange([10,20,30]) == -1  # Strictly increasing array
