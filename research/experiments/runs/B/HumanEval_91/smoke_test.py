from solution import is_bored

# Test cases from the docstring
assert is_bored("Hello world") == 0
assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1

# Additional test cases
assert is_bored("I am happy") == 1
assert is_bored("I. I. I.") == 3
assert is_bored("Island") == 0
assert is_bored("I'm happy") == 1
assert is_bored("I am very happy. I am excited!") == 2
assert is_bored("") == 0
assert is_bored("I") == 1
assert is_bored("I?") == 1
assert is_bored("I!") == 1
assert is_bored("Hi. I am here.") == 1
assert is_bored("It is sunny. I like it.") == 1
assert is_bored("Wow! I am impressed!") == 1
assert is_bored("Island of happiness") == 0
