from solution import rounded_avg

# Test cases from docstring
assert rounded_avg(1, 5) == "0b11"
assert rounded_avg(7, 5) == -1
assert rounded_avg(10, 20) == "0b1111"
assert rounded_avg(20, 33) == "0b11010"

# Additional edge cases
assert rounded_avg(1, 1) == "0b1"
assert rounded_avg(1, 2) == "0b10"
assert rounded_avg(2, 3) == "0b10"
assert rounded_avg(3, 4) == "0b100"
