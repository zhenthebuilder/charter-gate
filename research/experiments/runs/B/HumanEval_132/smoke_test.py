from solution import is_nested

assert is_nested('[[]]') == True, "Failed: [[]]"
assert is_nested('[]]]]]]][[[[[]') == False, "Failed: []]]]]]][[[[[]"
assert is_nested('[][]') == False, "Failed: [][]"
assert is_nested('[]') == False, "Failed: []"
assert is_nested('[[][]]') == True, "Failed: [[][]]"
assert is_nested('[[]][[') == True, "Failed: [[]][["

# Additional edge cases
assert is_nested('') == False, "Failed: empty string"
assert is_nested('[[[') == False, "Failed: unmatched open brackets"
assert is_nested(']]]') == False, "Failed: unmatched close brackets"
assert is_nested('[[[[[') == False, "Failed: all open brackets"
assert is_nested('[[[]]') == True, "Failed: [[[]]"
assert is_nested('[[[[]]]]') == True, "Failed: [[[[]]]]"
assert is_nested('[][][]') == False, "Failed: [][][]"
assert is_nested('[[[][]]])') == True, "Failed: [[[][]]]"
