from solution import mean_absolute_deviation

# Docstring example
assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0

# Single element (deviation is 0)
assert mean_absolute_deviation([5.0]) == 0.0

# All identical elements (all deviations are 0)
assert mean_absolute_deviation([3.0, 3.0, 3.0]) == 0.0

# Two-element list: [2, 4], mean=3, deviations=[1, 1], MAD=1
assert mean_absolute_deviation([2.0, 4.0]) == 1.0

# Negative numbers: [-1, 0, 1], mean=0, deviations=[1, 0, 1], MAD=2/3
assert abs(mean_absolute_deviation([-1.0, 0.0, 1.0]) - 2/3) < 1e-9
