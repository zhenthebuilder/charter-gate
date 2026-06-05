from solution import eat

# Test docstring examples
assert eat(5, 6, 10) == [11, 4]
assert eat(4, 8, 9) == [12, 1]
assert eat(1, 10, 10) == [11, 0]
assert eat(2, 11, 5) == [7, 0]

# Edge cases
assert eat(0, 0, 0) == [0, 0]
assert eat(0, 5, 0) == [0, 0]  # need > remaining, eat nothing
assert eat(10, 0, 5) == [10, 5]  # need = 0, eat nothing
assert eat(100, 50, 1000) == [150, 950]  # plenty available

print("All tests passed!")
