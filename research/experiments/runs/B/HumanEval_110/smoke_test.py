from solution import exchange

# Examples from docstring
assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
assert exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"

# All even in lst1 already
assert exchange([2, 4, 6], [1, 3, 5]) == "YES"

# All odd in lst1, sufficient evens in lst2
assert exchange([1, 3, 5], [2, 4, 6]) == "YES"

# All odd in lst1, insufficient evens in lst2
assert exchange([1, 3, 5, 7], [2, 4]) == "NO"

# Exactly enough evens to match odds
assert exchange([1, 3], [2, 4]) == "YES"

# Single element cases
assert exchange([1], [2]) == "YES"
assert exchange([1], [1]) == "NO"
assert exchange([2], [1]) == "YES"

# More evens available than needed
assert exchange([1, 3], [2, 4, 6, 8, 10]) == "YES"
