from solution import find_zero, poly

# Test example 1: f(x) = 1 + 2x, expect x = -0.5
result1 = find_zero([1, 2])
assert round(result1, 2) == -0.5

# Test example 2: f(x) = -6 + 11x - 6x^2 + x^3, expect one of [1, 2, 3]
result2 = find_zero([-6, 11, -6, 1])
assert round(result2, 2) in [1.0, 2.0, 3.0]

# Verify results are actual zeros
assert abs(poly([1, 2], result1)) < 1e-6
assert abs(poly([-6, 11, -6, 1], result2)) < 1e-6
