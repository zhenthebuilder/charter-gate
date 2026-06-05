from solution import factorize

# Test basic examples from docstring
assert factorize(8) == [2, 2, 2]
assert factorize(25) == [5, 5]
assert factorize(70) == [2, 5, 7]

# Test edge cases
assert factorize(1) == []
assert factorize(2) == [2]
assert factorize(13) == [13]
assert factorize(100) == [2, 2, 5, 5]
assert factorize(15) == [3, 5]
