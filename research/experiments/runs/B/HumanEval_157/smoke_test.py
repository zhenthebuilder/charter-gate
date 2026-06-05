from solution import right_angle_triangle

# Test the given examples
assert right_angle_triangle(3, 4, 5) == True
assert right_angle_triangle(1, 2, 3) == False

# Test with different order
assert right_angle_triangle(5, 3, 4) == True
assert right_angle_triangle(4, 5, 3) == True

# Test other Pythagorean triples
assert right_angle_triangle(6, 8, 10) == True
assert right_angle_triangle(5, 12, 13) == True

# Test non-right-angled triangles
assert right_angle_triangle(1, 1, 1) == False
assert right_angle_triangle(2, 2, 2) == False
assert right_angle_triangle(3, 4, 6) == False
