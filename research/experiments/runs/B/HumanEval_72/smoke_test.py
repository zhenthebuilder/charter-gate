from solution import will_it_fly

# Examples from docstring
assert will_it_fly([1, 2], 5) == False
assert will_it_fly([3, 2, 3], 1) == False
assert will_it_fly([3, 2, 3], 9) == True
assert will_it_fly([3], 5) == True

# Additional cases
assert will_it_fly([], 0) == True  # Empty list is palindromic
assert will_it_fly([1, 1], 2) == True  # Even-length palindrome, exact weight
assert will_it_fly([1, 2, 1], 4) == True  # Odd-length palindrome
assert will_it_fly([1, 2, 1], 3) == False  # Palindrome but sum exceeds weight
assert will_it_fly([1, 2, 3, 2, 1], 9) == True  # Longer palindrome
assert will_it_fly([5, 5], 10) == True  # Palindrome with equal elements
assert will_it_fly([5, 5], 9) == False  # Palindrome but weight insufficient
