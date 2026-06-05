from solution import move_one_ball

# Examples from docstring
assert move_one_ball([3, 4, 5, 1, 2]) == True
assert move_one_ball([3, 5, 4, 1, 2]) == False

# Edge cases
assert move_one_ball([]) == True
assert move_one_ball([1]) == True
assert move_one_ball([1, 2, 3]) == True

# Already sorted
assert move_one_ball([1, 2, 3, 4, 5]) == True

# Single break point (valid rotations)
assert move_one_ball([2, 3, 4, 5, 1]) == True
assert move_one_ball([5, 1, 2, 3, 4]) == True
assert move_one_ball([2, 1]) == True

# Multiple break points (invalid)
assert move_one_ball([3, 2, 1]) == False
assert move_one_ball([2, 1, 3, 4]) == False
assert move_one_ball([3, 1, 4, 2]) == False
