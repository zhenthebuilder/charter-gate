from solution import strange_sort_list

# Test cases from docstring
assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
assert strange_sort_list([]) == []

# Additional cases
assert strange_sort_list([1]) == [1]
assert strange_sort_list([1, 2]) == [1, 2]
assert strange_sort_list([2, 1]) == [1, 2]
assert strange_sort_list([10, 5]) == [5, 10]
assert strange_sort_list([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 9, 1, 6, 2, 5, 3, 4]
assert strange_sort_list([-1, -2, 0, 1, 2]) == [-2, 2, -1, 1, 0]
