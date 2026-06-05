from solution import find_max

assert find_max(["name", "of", "string"]) == "string"
assert find_max(["name", "enam", "game"]) == "enam"
assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
assert find_max(["hello"]) == "hello"
assert find_max(["abc", "bcd"]) == "abc"
assert find_max(["dog", "god", "cat"]) == "cat"
