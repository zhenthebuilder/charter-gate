from solution import solve

# Test cases from the docstring
assert solve("1234") == "4321"
assert solve("ab") == "AB"
assert solve("#a@C") == "#A@c"

# Additional test cases
assert solve("") == ""
assert solve("A") == "a"
assert solve("a") == "A"
assert solve("ABC") == "abc"
assert solve("123!@#") == "#@!321"
assert solve("aB1Cd") == "Ab1cD"
assert solve("!@#") == "#@!"
assert solve("Hello World!") == "hELLO wORLD!"
