from solution import is_happy

# Docstring examples
assert is_happy("a") == False
assert is_happy("aa") == False
assert is_happy("abcd") == True
assert is_happy("aabb") == False
assert is_happy("adb") == True
assert is_happy("xyy") == False

# Additional cases from specification
assert is_happy("abc") == True
assert is_happy("abcdef") == True
assert is_happy("abca") == True
assert is_happy("abcaa") == False
assert is_happy("aaa") == False
assert is_happy("aba") == False
assert is_happy("xyz") == True
assert is_happy("xxyy") == False
