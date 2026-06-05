from solution import rescale_to_unit


def approx_equal(a, b, tol=1e-9):
    return abs(a - b) < tol


# Test the docstring example
result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
expected = [0.0, 0.25, 0.5, 0.75, 1.0]
assert all(approx_equal(r, e) for r, e in zip(result, expected))

# Test with two elements (minimum case)
result = rescale_to_unit([0.0, 10.0])
expected = [0.0, 1.0]
assert all(approx_equal(r, e) for r, e in zip(result, expected))

# Test with negative numbers
result = rescale_to_unit([-5.0, 0.0, 5.0])
expected = [0.0, 0.5, 1.0]
assert all(approx_equal(r, e) for r, e in zip(result, expected))

# Test with duplicate min/max values
result = rescale_to_unit([2.0, 5.0, 2.0])
expected = [0.0, 1.0, 0.0]
assert all(approx_equal(r, e) for r, e in zip(result, expected))

# Test with mixed negative and positive
result = rescale_to_unit([-10.0, -5.0, 0.0, 5.0, 10.0])
expected = [0.0, 0.25, 0.5, 0.75, 1.0]
assert all(approx_equal(r, e) for r, e in zip(result, expected))
