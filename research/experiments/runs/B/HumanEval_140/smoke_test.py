from solution import fix_spaces

# From docstring examples
assert fix_spaces("Example") == "Example"
assert fix_spaces("Example 1") == "Example_1"
assert fix_spaces(" Example 2") == "_Example_2"
assert fix_spaces(" Example   3") == "_Example-3"

# Additional cases
assert fix_spaces("") == ""
assert fix_spaces("a  b") == "a__b"
assert fix_spaces("a   b") == "a-b"
assert fix_spaces("    a") == "-a"
assert fix_spaces("a    b    c") == "a-b-c"
