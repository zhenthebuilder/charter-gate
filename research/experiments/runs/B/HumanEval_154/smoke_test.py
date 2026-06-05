from solution import cycpattern_check

# Test cases from docstring
assert cycpattern_check("abcd", "abd") == False
assert cycpattern_check("hello", "ell") == True
assert cycpattern_check("whassup", "psus") == False
assert cycpattern_check("abab", "baa") == True
assert cycpattern_check("efef", "eeff") == False
assert cycpattern_check("himenss", "simen") == True

# Additional edge cases
assert cycpattern_check("a", "a") == True
assert cycpattern_check("abc", "a") == True
assert cycpattern_check("abc", "abc") == True
assert cycpattern_check("ab", "ba") == True
assert cycpattern_check("abc", "def") == False
