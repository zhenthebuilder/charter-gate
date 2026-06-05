from solution import match_parens

# Examples from docstring
assert match_parens(['()(', ')']) == 'Yes'
assert match_parens([')', ')']) == 'No'

# Extra test cases
assert match_parens(['()', '()']) == 'Yes'
assert match_parens(['((', '))']) == 'Yes'
assert match_parens(['(', '(']) == 'No'
assert match_parens([')', '(']) == 'Yes'
assert match_parens(['(())', '(())']) == 'Yes'
assert match_parens(['()', ')']) == 'No'
