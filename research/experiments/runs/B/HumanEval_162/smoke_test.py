from solution import string_to_md5

# Test from docstring
assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

# Test empty string returns None
assert string_to_md5('') is None

# Additional test cases with well-known MD5 values
assert string_to_md5('a') == '0cc175b9c0f1b6a831c399e269772661'
assert string_to_md5('abc') == '900150983cd24fb0d6963f7d28e17f72'
