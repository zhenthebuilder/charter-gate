from solution import x_or_y

# Test examples from docstring
assert x_or_y(7, 34, 12) == 34
assert x_or_y(15, 8, 5) == 5

# Additional test cases for prime numbers
assert x_or_y(2, 10, 20) == 10   # 2 is prime
assert x_or_y(3, 10, 20) == 10   # 3 is prime
assert x_or_y(5, 10, 20) == 10   # 5 is prime
assert x_or_y(11, 10, 20) == 10  # 11 is prime
assert x_or_y(13, 10, 20) == 10  # 13 is prime

# Additional test cases for non-prime numbers
assert x_or_y(1, 10, 20) == 20   # 1 is not prime
assert x_or_y(0, 10, 20) == 20   # 0 is not prime
assert x_or_y(4, 10, 20) == 20   # 4 is not prime
assert x_or_y(6, 10, 20) == 20   # 6 is not prime
assert x_or_y(8, 10, 20) == 20   # 8 is not prime
assert x_or_y(9, 10, 20) == 20   # 9 is not prime
assert x_or_y(10, 10, 20) == 20  # 10 is not prime
