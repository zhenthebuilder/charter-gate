from solution import how_many_times

# Test cases from docstring
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3

# Additional overlapping cases
assert how_many_times('ababa', 'aba') == 2
assert how_many_times('ababab', 'ab') == 3
assert how_many_times('aaaaaa', 'aa') == 5

# Non-overlapping and non-matching cases
assert how_many_times('abcabc', 'abc') == 2
assert how_many_times('abc', 'z') == 0
assert how_many_times('x', 'x') == 1

# Edge cases
assert how_many_times('aaa', '') == 0
assert how_many_times('', '') == 0
