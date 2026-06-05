from solution import int_to_mini_roman

# Examples from docstring
assert int_to_mini_roman(19) == 'xix'
assert int_to_mini_roman(152) == 'clii'
assert int_to_mini_roman(426) == 'cdxxvi'

# Edge cases
assert int_to_mini_roman(1) == 'i'
assert int_to_mini_roman(1000) == 'm'

# Single value mappings
assert int_to_mini_roman(4) == 'iv'
assert int_to_mini_roman(5) == 'v'
assert int_to_mini_roman(9) == 'ix'
assert int_to_mini_roman(10) == 'x'
assert int_to_mini_roman(40) == 'xl'
assert int_to_mini_roman(50) == 'l'
assert int_to_mini_roman(90) == 'xc'
assert int_to_mini_roman(100) == 'c'
assert int_to_mini_roman(400) == 'cd'
assert int_to_mini_roman(500) == 'd'
assert int_to_mini_roman(900) == 'cm'

# Other representative cases
assert int_to_mini_roman(3) == 'iii'
assert int_to_mini_roman(8) == 'viii'
assert int_to_mini_roman(27) == 'xxvii'
assert int_to_mini_roman(58) == 'lviii'
assert int_to_mini_roman(1994) == 'mcmxciv'
