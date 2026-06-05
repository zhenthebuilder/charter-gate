from solution import decimal_to_binary

# Test cases from docstring
assert decimal_to_binary(15) == "db1111db"
assert decimal_to_binary(32) == "db100000db"

# Additional test cases
assert decimal_to_binary(0) == "db0db"
assert decimal_to_binary(1) == "db1db"
assert decimal_to_binary(2) == "db10db"
assert decimal_to_binary(8) == "db1000db"
assert decimal_to_binary(255) == "db11111111db"
