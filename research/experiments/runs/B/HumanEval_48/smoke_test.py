from solution import is_palindrome

# Test docstring examples
assert is_palindrome('') == True
assert is_palindrome('aba') == True
assert is_palindrome('aaaaa') == True
assert is_palindrome('zbcd') == False

# Additional test cases
assert is_palindrome('a') == True
assert is_palindrome('aa') == True
assert is_palindrome('ab') == False
assert is_palindrome('racecar') == True
assert is_palindrome('hello') == False
assert is_palindrome('noon') == True
