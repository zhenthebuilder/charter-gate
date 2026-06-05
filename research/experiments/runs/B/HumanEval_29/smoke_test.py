from solution import filter_by_prefix

# Docstring examples
assert filter_by_prefix([], 'a') == []
assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

# Additional cases
assert filter_by_prefix(['apple', 'apricot', 'banana'], 'a') == ['apple', 'apricot']
assert filter_by_prefix(['apple', 'apricot', 'banana'], 'b') == ['banana']
assert filter_by_prefix(['apple', 'apricot', 'banana'], 'c') == []
assert filter_by_prefix(['hello', 'world'], 'he') == ['hello']
assert filter_by_prefix(['hello', 'world'], '') == ['hello', 'world']
assert filter_by_prefix(['a', 'ab', 'abc'], 'a') == ['a', 'ab', 'abc']
assert filter_by_prefix(['cat', 'car', 'dog'], 'ca') == ['cat', 'car']
assert filter_by_prefix(['Apple', 'apple'], 'a') == ['apple']
assert filter_by_prefix(['Apple', 'apple'], 'A') == ['Apple']
