from solution import triangle_area
import math

# Test examples from docstring
assert triangle_area(3, 4, 5) == 6.00
assert triangle_area(1, 2, 10) == -1

# Test equilateral triangle with side 2
assert triangle_area(2, 2, 2) == round(math.sqrt(3), 2)

# Test isosceles triangle
assert triangle_area(5, 5, 6) == 12.0

# Test boundary case: sum of two sides equals third (invalid)
assert triangle_area(1, 2, 3) == -1

# Test different orderings of valid triangle
assert triangle_area(4, 3, 5) == 6.00

# Test another invalid triangle
assert triangle_area(1, 1, 5) == -1
