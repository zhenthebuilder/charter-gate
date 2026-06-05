from solution import even_odd_palindrome

# Test from docstring Example 1
assert even_odd_palindrome(3) == (1, 2)

# Test from docstring Example 2
assert even_odd_palindrome(12) == (4, 6)

# Additional test cases
assert even_odd_palindrome(1) == (0, 1)  # only 1
assert even_odd_palindrome(2) == (1, 1)  # 1, 2
assert even_odd_palindrome(9) == (4, 5)  # all single digits: 2,4,6,8 vs 1,3,5,7,9
assert even_odd_palindrome(11) == (4, 6)  # adds 11 (odd palindrome)
assert even_odd_palindrome(100) == (8, 10)  # 1-9 + 11,22,33,44,55,66,77,88,99
