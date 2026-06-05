from solution import encode

# Test examples from docstring
assert encode('test') == 'TGST'
assert encode('This is a message') == 'tHKS KS C MGSSCGG'

# Test individual vowels
assert encode('a') == 'C'
assert encode('A') == 'c'
assert encode('e') == 'G'
assert encode('E') == 'g'
assert encode('i') == 'K'
assert encode('I') == 'k'
assert encode('o') == 'Q'
assert encode('O') == 'q'
assert encode('u') == 'W'
assert encode('U') == 'w'

# Test consonants (case swaps)
assert encode('b') == 'B'
assert encode('B') == 'b'

# Test edge cases
assert encode('') == ''
assert encode('xyz') == 'XYZ'
assert encode('aeiou') == 'CGKQW'
assert encode('Hello') == 'hGLLQ'
