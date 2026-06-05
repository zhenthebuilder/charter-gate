from solution import find_closest_elements

# Examples from docstring
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

# Additional test cases
assert find_closest_elements([1.0, 2.0]) == (1.0, 2.0)
assert find_closest_elements([10.0, 1.0, 1.5, 20.0]) == (1.0, 1.5)
assert find_closest_elements([5.0, 1.0, 1.0]) == (1.0, 1.0)
assert find_closest_elements([-5.0, -4.9, 0.0]) == (-5.0, -4.9)
assert find_closest_elements([0.1, 0.2, 0.15]) == (0.1, 0.15)
