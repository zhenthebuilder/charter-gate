from solution import string_xor

# Test from docstring
assert string_xor('010', '110') == '100'

# Additional test cases
assert string_xor('0', '0') == '0'
assert string_xor('1', '1') == '0'
assert string_xor('1', '0') == '1'
assert string_xor('0', '1') == '1'
assert string_xor('1111', '1111') == '0000'
assert string_xor('1111', '0000') == '1111'
assert string_xor('1010', '0101') == '1111'
assert string_xor('0000', '0000') == '0000'
