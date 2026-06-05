from solution import do_algebra

# Test from docstring example
assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

# Single operations
assert do_algebra(['+'], [2, 3]) == 5
assert do_algebra(['-'], [5, 2]) == 3
assert do_algebra(['*'], [3, 4]) == 12
assert do_algebra(['//'], [7, 2]) == 3
assert do_algebra(['**'], [2, 3]) == 8

# Multiple operations
assert do_algebra(['+', '+'], [1, 2, 3]) == 6
assert do_algebra(['-', '-'], [10, 3, 2]) == 5

# Order of operations (multiplication before addition)
assert do_algebra(['+', '*'], [2, 3, 4]) == 14

# Order of operations (exponentiation before multiplication)
assert do_algebra(['*', '**'], [2, 3, 2]) == 18

# Order of operations (all operators)
assert do_algebra(['+', '*', '-', '//'], [10, 2, 3, 4, 2]) == 14
