from solution import get_odd_collatz

assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(2) == [1]
assert get_odd_collatz(3) == [1, 3, 5]
assert get_odd_collatz(10) == [1, 5]
assert get_odd_collatz(12) == [1, 3, 5]
