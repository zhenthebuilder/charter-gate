from solution import split_words

# From docstring examples
assert split_words("Hello world!") == ["Hello", "world!"]
assert split_words("Hello,world!") == ["Hello", "world!"]
assert split_words("abcdef") == 3

# Whitespace takes priority over commas
assert split_words("a,b c,d") == ["a,b", "c,d"]

# Only uppercase (no lowercase letters)
assert split_words("ABCDEF") == 0

# Mixed case - only count lowercase odd-positioned
assert split_words("AbCdEf") == 3

# Single characters
assert split_words("b") == 1
assert split_words("a") == 0

# Multiple commas
assert split_words("a,b,c") == ["a", "b", "c"]

# Special characters only
assert split_words("!@#$") == 0

# All odd-positioned letters
assert split_words("bdf") == 3

# All even-positioned letters
assert split_words("ace") == 0

# Mixed odd and even
assert split_words("abc") == 1
