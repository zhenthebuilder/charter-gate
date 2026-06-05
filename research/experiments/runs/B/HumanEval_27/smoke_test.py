from solution import flip_case

# Test from docstring
assert flip_case('Hello') == 'hELLO'

# Additional test cases
assert flip_case('') == ''
assert flip_case('hello') == 'HELLO'
assert flip_case('HELLO') == 'hello'
assert flip_case('a') == 'A'
assert flip_case('A') == 'a'
assert flip_case('Hello123') == 'hELLO123'
assert flip_case('Hello!World') == 'hELLO!wORLD'
assert flip_case('123!@#') == '123!@#'
