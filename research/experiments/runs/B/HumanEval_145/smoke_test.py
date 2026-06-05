from solution import order_by_points

assert order_by_points([]) == []
assert order_by_points([5]) == [5]
assert order_by_points([1, 11, 111]) == [1, 11, 111]
assert order_by_points([100, 2]) == [100, 2]
assert order_by_points([1, -1]) == [1, -1]
assert order_by_points([11, 20]) == [11, 20]
assert order_by_points([5, 15, 10]) == [10, 5, 15]
assert order_by_points([-1, -11, 1, 11, -12]) == [-1, 1, -11, 11, -12]
