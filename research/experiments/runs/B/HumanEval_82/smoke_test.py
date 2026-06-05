from solution import prime_length

# Examples from docstring
assert prime_length('Hello') == True
assert prime_length('abcdcba') == True
assert prime_length('kittens') == True
assert prime_length('orange') == False

# Additional test cases
assert prime_length('') == False
assert prime_length('a') == False
assert prime_length('ab') == True
assert prime_length('abc') == True
assert prime_length('abcd') == False
assert prime_length('abcdef') == False
assert prime_length('abcdefghijk') == True
