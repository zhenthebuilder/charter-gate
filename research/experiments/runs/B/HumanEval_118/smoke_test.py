from solution import get_closest_vowel

# Docstring examples
assert get_closest_vowel("yogurt") == "u"
assert get_closest_vowel("FULL") == "U"
assert get_closest_vowel("quick") == ""
assert get_closest_vowel("ab") == ""

# Additional cases
assert get_closest_vowel("reason") == "o"
assert get_closest_vowel("testing") == "i"
assert get_closest_vowel("bac") == "a"
assert get_closest_vowel("aeiou") == ""
assert get_closest_vowel("bcdfg") == ""
