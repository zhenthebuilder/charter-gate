from solution import filter_by_substring

# Examples from docstring
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

# Additional confident test cases
assert filter_by_substring(['hello', 'world'], 'o') == ['hello', 'world']
assert filter_by_substring(['hello', 'world'], 'xyz') == []
assert filter_by_substring(['a', 'b', 'c'], 'a') == ['a']
assert filter_by_substring(['abc', 'abc', 'abc'], 'bc') == ['abc', 'abc', 'abc']
assert filter_by_substring(['test', 'testing', 'tested'], 'test') == ['test', 'testing', 'tested']
