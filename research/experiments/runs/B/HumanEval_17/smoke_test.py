from solution import parse_music

# Test the example from the docstring
assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

# Single notes
assert parse_music('o') == [4]
assert parse_music('o|') == [2]
assert parse_music('.|') == [1]

# Multiple notes
assert parse_music('o o') == [4, 4]
assert parse_music('o| o|') == [2, 2]
assert parse_music('.| .| .|') == [1, 1, 1]
assert parse_music('o o| .|') == [4, 2, 1]
