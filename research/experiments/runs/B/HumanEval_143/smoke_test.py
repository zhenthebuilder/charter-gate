from solution import words_in_sentence

# Examples from docstring
assert words_in_sentence("This is a test") == "is"
assert words_in_sentence("lets go for swimming") == "go for"

# Length 2 (prime)
assert words_in_sentence("go") == "go"
assert words_in_sentence("hi there") == "hi there"

# Length 3 (prime)
assert words_in_sentence("cat") == "cat"
assert words_in_sentence("cat dog") == "cat dog"

# Length 5 (prime)
assert words_in_sentence("hello") == "hello"

# Length 7 (prime)
assert words_in_sentence("testing") == "testing"

# No prime lengths
assert words_in_sentence("test") == ""
assert words_in_sentence("bird fish") == ""
