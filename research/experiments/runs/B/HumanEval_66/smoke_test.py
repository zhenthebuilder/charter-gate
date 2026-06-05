from solution import digitSum

# Examples from docstring
assert digitSum("") == 0
assert digitSum("abAB") == 131
assert digitSum("abcCd") == 67
assert digitSum("helloE") == 69
assert digitSum("woArBld") == 131
assert digitSum("aAaaaXa") == 153

# Extra cases
assert digitSum("A") == 65
assert digitSum("ABC") == 65 + 66 + 67
assert digitSum("aabbcc") == 0
