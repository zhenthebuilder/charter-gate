from solution import count_up_to

assert count_up_to(5) == [2, 3]
assert count_up_to(11) == [2, 3, 5, 7]
assert count_up_to(0) == []
assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
assert count_up_to(1) == []
assert count_up_to(18) == [2, 3, 5, 7, 11, 13, 17]

# Additional cases
assert count_up_to(2) == []
assert count_up_to(3) == [2]
assert count_up_to(4) == [2, 3]
assert count_up_to(10) == [2, 3, 5, 7]
