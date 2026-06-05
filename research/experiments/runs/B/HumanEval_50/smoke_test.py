from solution import decode_shift

def encode_shift(s: str):
    """Helper to verify decode_shift works correctly"""
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

# Round-trip test: encoding then decoding should recover original
assert decode_shift(encode_shift("hello")) == "hello"
assert decode_shift(encode_shift("abc")) == "abc"
assert decode_shift(encode_shift("xyz")) == "xyz"

# All lowercase letters
assert decode_shift(encode_shift("abcdefghijklmnopqrstuvwxyz")) == "abcdefghijklmnopqrstuvwxyz"

# Edge cases
assert decode_shift(encode_shift("")) == ""
assert decode_shift(encode_shift("a")) == "a"
assert decode_shift(encode_shift("z")) == "z"

# Specific known mappings (encode_shift shifts by 5)
# 'a' encodes to 'f', so 'f' should decode to 'a'
assert decode_shift("f") == "a"
# 'z' encodes to 'e' (wraps: 25+5=30, 30%26=4='e')
assert decode_shift("e") == "z"
# 'y' encodes to 'd' (wraps: 24+5=29, 29%26=3='d')
assert decode_shift("d") == "y"
