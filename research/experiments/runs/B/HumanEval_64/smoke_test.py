from solution import vowels_count

# Docstring examples
assert vowels_count("abcde") == 2
assert vowels_count("ACEDY") == 3

# Edge cases
assert vowels_count("") == 0
assert vowels_count("bcdfg") == 0
assert vowels_count("aeiou") == 5
assert vowels_count("y") == 1
assert vowels_count("xyz") == 0  # y not at end
assert vowels_count("happy") == 2  # a + y at end
assert vowels_count("yes") == 1  # e only (y not at end)
assert vowels_count("rhythm") == 0  # y not at end, no other vowels
assert vowels_count("day") == 2  # a + y at end
assert vowels_count("beauty") == 4  # e, a, u, y at end
assert vowels_count("gymnasium") == 3  # a, i, u (y not at end)
assert vowels_count("copy") == 2  # o + y at end
assert vowels_count("yellow") == 2  # e, o (y not at end)
