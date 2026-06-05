from solution import solution

# Test cases from docstring
assert solution([5, 8, 7, 1]) == 12
assert solution([3, 3, 3, 3, 3]) == 9
assert solution([30, 13, 24, 321]) == 0

# Additional test cases
assert solution([1]) == 1  # Single odd element at position 0
assert solution([2]) == 0  # Single even element at position 0
assert solution([1, 2, 3, 4]) == 4  # 1 at position 0 (odd), 3 at position 2 (odd)
assert solution([2, 3, 4, 5]) == 0  # Positions 0 and 2 have even numbers
assert solution([7, 8, 9, 10, 11]) == 27  # Positions 0, 2, 4 have 7, 9, 11
