from solution import choose_num

# Documented examples
assert choose_num(12, 15) == 14
assert choose_num(13, 12) == -1

# Invalid range (x > y)
assert choose_num(15, 13) == -1

# x and y are both even
assert choose_num(2, 4) == 4
assert choose_num(10, 20) == 20

# x is even, y is odd
assert choose_num(2, 5) == 4
assert choose_num(10, 15) == 14

# x is odd, y is even
assert choose_num(1, 4) == 4
assert choose_num(11, 14) == 14

# x is odd, y is odd (with valid even in range)
assert choose_num(1, 5) == 4
assert choose_num(11, 15) == 14

# Single even element
assert choose_num(2, 2) == 2
assert choose_num(10, 10) == 10

# Single odd element
assert choose_num(1, 1) == -1
assert choose_num(5, 5) == -1

# Odd endpoints with no even between them
assert choose_num(13, 13) == -1
assert choose_num(15, 15) == -1

# Two odd numbers with even between
assert choose_num(13, 15) == 14
