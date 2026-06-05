from solution import reverse_delete

# Example 1
result, is_palindrome = reverse_delete("abcde", "ae")
assert result == "bcd"
assert is_palindrome == False

# Example 2
result, is_palindrome = reverse_delete("abcdef", "b")
assert result == "acdef"
assert is_palindrome == False

# Example 3
result, is_palindrome = reverse_delete("abcdedcba", "ab")
assert result == "cdedc"
assert is_palindrome == True

# Edge case: all characters deleted
result, is_palindrome = reverse_delete("aaa", "a")
assert result == ""
assert is_palindrome == True

# Edge case: single character remains
result, is_palindrome = reverse_delete("abc", "bc")
assert result == "a"
assert is_palindrome == True

# Edge case: nothing deleted, result is palindrome
result, is_palindrome = reverse_delete("racecar", "xyz")
assert result == "racecar"
assert is_palindrome == True

# Edge case: nothing deleted, result is not palindrome
result, is_palindrome = reverse_delete("abc", "xyz")
assert result == "abc"
assert is_palindrome == False
