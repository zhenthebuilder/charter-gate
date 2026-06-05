from solution import simplify

# Test cases from docstring
assert simplify("1/5", "5/1") == True
assert simplify("1/6", "2/1") == False
assert simplify("7/10", "10/2") == False

# Additional test cases
assert simplify("2/3", "3/2") == True  # (2*3)/(3*2) = 1
assert simplify("1/1", "1/1") == True  # 1 * 1 = 1
assert simplify("1/2", "2/1") == True  # (1*2)/(2*1) = 1
assert simplify("1/3", "1/1") == False  # 1/3 is not whole
assert simplify("2/3", "1/2") == False  # (2*1)/(3*2) = 1/3, not whole
assert simplify("5/6", "6/5") == True  # (5*6)/(6*5) = 1
assert simplify("1/4", "2/1") == False  # (1*2)/(4*1) = 1/2, not whole
