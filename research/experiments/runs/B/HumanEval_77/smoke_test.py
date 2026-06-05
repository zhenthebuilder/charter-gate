from solution import iscube

# Test examples from docstring
assert iscube(1) == True
assert iscube(2) == False
assert iscube(-1) == True
assert iscube(64) == True
assert iscube(0) == True
assert iscube(180) == False

# Additional test cases
assert iscube(8) == True
assert iscube(27) == True
assert iscube(-8) == True
assert iscube(-27) == True
assert iscube(125) == True
assert iscube(-125) == True
assert iscube(100) == False
