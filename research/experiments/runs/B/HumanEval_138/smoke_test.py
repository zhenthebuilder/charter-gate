from solution import is_equal_to_sum_even

# Test cases from docstring
assert is_equal_to_sum_even(4) == False
assert is_equal_to_sum_even(6) == False
assert is_equal_to_sum_even(8) == True

# Additional test cases
assert is_equal_to_sum_even(10) == True  # 2 + 2 + 2 + 4
assert is_equal_to_sum_even(12) == True  # 2 + 2 + 2 + 6
assert is_equal_to_sum_even(14) == True  # 2 + 2 + 2 + 8
assert is_equal_to_sum_even(1) == False  # Too small
assert is_equal_to_sum_even(2) == False  # Too small
assert is_equal_to_sum_even(7) == False  # Odd
assert is_equal_to_sum_even(9) == False  # Odd
assert is_equal_to_sum_even(100) == True  # 2 + 2 + 2 + 94
