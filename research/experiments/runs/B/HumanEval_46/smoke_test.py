from solution import fib4

# Test base cases
assert fib4(0) == 0
assert fib4(1) == 0
assert fib4(2) == 2
assert fib4(3) == 0

# Test docstring examples
assert fib4(5) == 4
assert fib4(6) == 8
assert fib4(7) == 14

# Additional test cases derived from the specification
assert fib4(4) == 2  # 0 + 0 + 2 + 0 = 2
assert fib4(8) == 28  # 14 + 8 + 4 + 2 = 28
assert fib4(9) == 54  # 28 + 14 + 8 + 4 = 54
