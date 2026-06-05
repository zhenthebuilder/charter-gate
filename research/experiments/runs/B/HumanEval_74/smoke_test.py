from solution import total_match

# Test examples from docstring
assert total_match([], []) == []
assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']

# Additional edge cases
assert total_match(['a'], ['b']) == ['a']  # Equal length, return first
assert total_match(['ab'], ['a']) == ['a']  # Second has fewer
assert total_match(['abc', 'def'], ['xy']) == ['xy']  # Second has fewer (2 vs 6)
assert total_match(['x'], ['y', 'z']) == ['x']  # First has fewer (1 vs 2)
