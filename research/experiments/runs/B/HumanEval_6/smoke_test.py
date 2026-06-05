from solution import parse_nested_parens

# Test the given example from docstring
assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]

# Test single groups with varying depths
assert parse_nested_parens('()') == [1]
assert parse_nested_parens('(())') == [2]
assert parse_nested_parens('((()))') == [3]
assert parse_nested_parens('(((())))') == [4]

# Test multiple groups
assert parse_nested_parens('() ()') == [1, 1]
assert parse_nested_parens('(()) ((()))') == [2, 3]

# Test mixed nesting patterns
assert parse_nested_parens('()(()) ()()()') == [2, 1]
