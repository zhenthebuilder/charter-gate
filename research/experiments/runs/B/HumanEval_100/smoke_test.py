from solution import make_a_pile

# Test from docstring
assert make_a_pile(3) == [3, 5, 7]

# Test with n=1
assert make_a_pile(1) == [1]

# Test with n=2 (even starting number)
assert make_a_pile(2) == [2, 4]

# Test with n=4 (even, multiple levels)
assert make_a_pile(4) == [4, 6, 8, 10]

# Test with n=5 (odd, multiple levels)
assert make_a_pile(5) == [5, 7, 9, 11, 13]

# Test with n=6
assert make_a_pile(6) == [6, 8, 10, 12, 14, 16]
