from solution import any_int

assert any_int(5, 2, 7) == True
assert any_int(3, 2, 2) == False
assert any_int(3, -2, 1) == True
assert any_int(3.6, -2.2, 2) == False
assert any_int(1, 1, 2) == True
assert any_int(0, 0, 0) == True
assert any_int(10, 5, 5) == True
assert any_int(1, 2, 4) == False
assert any_int(-1, -1, -2) == True
assert any_int(1.5, 2, 3.5) == False
