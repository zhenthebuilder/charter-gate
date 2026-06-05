from solution import anti_shuffle

# Examples from docstring
assert anti_shuffle('Hi') == 'Hi'
assert anti_shuffle('hello') == 'ehllo'
assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'

# Additional cases
assert anti_shuffle('') == ''
assert anti_shuffle('a') == 'a'
assert anti_shuffle('abc') == 'abc'
assert anti_shuffle('cba') == 'abc'
assert anti_shuffle('a b c') == 'a b c'
assert anti_shuffle('hello world') == 'ehllo dlorw'
assert anti_shuffle('BbAa') == 'ABab'
assert anti_shuffle('a  b') == 'a  b'
