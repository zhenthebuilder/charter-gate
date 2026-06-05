from solution import longest

# Docstring examples
assert longest([]) is None
assert longest(['a', 'b', 'c']) == 'a'
assert longest(['a', 'bb', 'ccc']) == 'ccc'

# Extra test cases
assert longest(['x']) == 'x'
assert longest(['hello', 'hi', 'hey', 'goodbye']) == 'goodbye'
assert longest(['aa', 'bb', 'cc']) == 'aa'
assert longest(['a', 'bb', 'c', 'ddd']) == 'ddd'
assert longest(['world', 'hello']) == 'world'
