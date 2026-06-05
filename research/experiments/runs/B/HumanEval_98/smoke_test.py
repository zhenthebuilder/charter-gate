from solution import count_upper

# Docstring examples
assert count_upper('aBCdEf') == 1
assert count_upper('abcdefg') == 0
assert count_upper('dBBE') == 0

# Edge cases
assert count_upper('') == 0
assert count_upper('A') == 1
assert count_upper('a') == 0
assert count_upper('B') == 0

# Additional cases
assert count_upper('AEIOU') == 3  # A, E, I at indices 0, 2, 4
assert count_upper('AaEeIiOoUu') == 5  # uppercase vowels at all even indices
assert count_upper('BCDFG') == 0
assert count_upper('EaIoU') == 3  # E, I, U at indices 0, 2, 4
