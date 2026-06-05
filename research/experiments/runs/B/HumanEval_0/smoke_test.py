from solution import has_close_elements

# Examples from docstring
assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True

# Edge cases
assert has_close_elements([], 0.5) == False
assert has_close_elements([1.0], 0.5) == False
assert has_close_elements([1.0, 2.0], 1.0) == False
assert has_close_elements([1.0, 1.9], 1.0) == True

# Additional cases
assert has_close_elements([1.0, 1.05], 0.1) == True
assert has_close_elements([0.0, 10.0, 20.0], 5.0) == False
assert has_close_elements([0.0, 1.0, 1.001], 0.01) == True
assert has_close_elements([-5.0, -4.96, 0.0], 0.05) == True
