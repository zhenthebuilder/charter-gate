from solution import double_the_difference

# Test cases from docstring
assert double_the_difference([1, 3, 2, 0]) == 10
assert double_the_difference([-1, -2, 0]) == 0
assert double_the_difference([9, -2]) == 81
assert double_the_difference([0]) == 0

# Additional test cases
assert double_the_difference([]) == 0
assert double_the_difference([1, 1, 1, 1]) == 4
assert double_the_difference([5]) == 25
assert double_the_difference([2, 4, 6]) == 0
assert double_the_difference([1.5, 2, 3]) == 9
assert double_the_difference([-1, -3, -5]) == 0
assert double_the_difference([7, 11]) == 170
