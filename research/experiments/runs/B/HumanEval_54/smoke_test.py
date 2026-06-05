from solution import same_chars

# Test cases from docstring
assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
assert same_chars('abcd', 'dddddddabc') == True
assert same_chars('dddddddabc', 'abcd') == True
assert same_chars('eabcd', 'dddddddabc') == False
assert same_chars('abcd', 'dddddddabce') == False
assert same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') == False

# Additional test cases
assert same_chars('', '') == True
assert same_chars('a', 'a') == True
assert same_chars('a', 'b') == False
assert same_chars('aaa', 'a') == True
assert same_chars('abc', 'bca') == True
assert same_chars('xyz', 'xyza') == False
