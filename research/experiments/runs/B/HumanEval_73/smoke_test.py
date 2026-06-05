from solution import smallest_change

# Test cases from docstring
assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 1]) == 0

# Additional test cases
assert smallest_change([]) == 0
assert smallest_change([1]) == 0
assert smallest_change([1, 1]) == 0
assert smallest_change([1, 2]) == 1
assert smallest_change([1, 2, 3, 4, 5]) == 2  # pairs: (1,5), (2,4) both mismatch
assert smallest_change([5, 4, 3, 4, 5]) == 0  # already palindrome
assert smallest_change([1, 1, 1, 2]) == 1  # (1,2) mismatch, middle pair matches

print("All tests passed!")
