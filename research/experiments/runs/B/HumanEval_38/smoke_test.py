from solution import decode_cyclic

# Empty string
assert decode_cyclic("") == ""

# Single character (not rotated)
assert decode_cyclic("a") == "a"

# Two characters (not rotated)
assert decode_cyclic("ab") == "ab"

# Three characters (rotated: "abc" -> "bca")
assert decode_cyclic("bca") == "abc"

# Six characters: "abcdef" -> "bca" + "efd"
assert decode_cyclic("bcaefd") == "abcdef"

# Seven characters: "abcdefg" -> "bca" + "efd" + "g"
assert decode_cyclic("bcaefdg") == "abcdefg"

# Nine characters: "abcdefghi" -> "bca" + "efd" + "hig"
assert decode_cyclic("bcaefdhig") == "abcdefghi"

# Four characters: "abcd" -> "bca" + "d"
assert decode_cyclic("bcad") == "abcd"

# Five characters: "abcde" -> "bca" + "de"
assert decode_cyclic("bcade") == "abcde"
