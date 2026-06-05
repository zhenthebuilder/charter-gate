from solution import count_nums

# Docstring examples
assert count_nums([]) == 0
assert count_nums([-1, 11, -11]) == 1
assert count_nums([1, 1, 2]) == 3

# Additional cases from specification
assert count_nums([-123]) == 1   # -1 + 2 + 3 = 4 > 0
assert count_nums([-10]) == 0    # -1 + 0 = -1, not > 0
assert count_nums([0]) == 0      # 0, not > 0
assert count_nums([5]) == 1      # 5 > 0
assert count_nums([-9, 9]) == 1  # -9 sum=-9, 9 sum=9
assert count_nums([100, -100]) == 1  # 100 sum=1, -100 sum=-1
assert count_nums([-99]) == 0    # -9 + 9 = 0, not > 0
