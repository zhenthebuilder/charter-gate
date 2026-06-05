from solution import digits

# Test cases from docstring
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15

# Single digit cases
assert digits(2) == 0
assert digits(3) == 3
assert digits(5) == 5
assert digits(7) == 7
assert digits(9) == 9
assert digits(6) == 0
assert digits(8) == 0

# Two digit cases
assert digits(13) == 3
assert digits(24) == 0
assert digits(35) == 15
assert digits(79) == 63

# All even digits
assert digits(2468) == 0
assert digits(2024) == 0

# All odd digits
assert digits(13579) == 945
assert digits(111) == 1
assert digits(333) == 27

# Mixed even and odd
assert digits(246813) == 3
assert digits(10) == 1
