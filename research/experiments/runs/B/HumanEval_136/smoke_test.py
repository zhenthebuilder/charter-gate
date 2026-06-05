from solution import largest_smallest_integers

assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
assert largest_smallest_integers([]) == (None, None)
assert largest_smallest_integers([0]) == (None, None)

assert largest_smallest_integers([-5, -2, 3, 8]) == (-2, 3)
assert largest_smallest_integers([-1, -10]) == (-1, None)
assert largest_smallest_integers([5, 10]) == (None, 5)
assert largest_smallest_integers([-3, -1, 0, 2, 4]) == (-1, 2)
assert largest_smallest_integers([-100, 1]) == (-100, 1)
