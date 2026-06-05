from solution import count_distinct_characters

# Docstring examples
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('Jerry') == 4

# Edge cases
assert count_distinct_characters('') == 0
assert count_distinct_characters('a') == 1
assert count_distinct_characters('aaaa') == 1
assert count_distinct_characters('AaBbCc') == 3

# Case-insensitivity verification
assert count_distinct_characters('AAaa') == 1
assert count_distinct_characters('aAbBcC') == 3

# Mixed with special characters
assert count_distinct_characters('Hello123') == 7
assert count_distinct_characters('a b c') == 4
