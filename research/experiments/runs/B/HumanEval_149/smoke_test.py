from solution import sorted_list_sum

# Examples from docstring
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

# Edge cases
assert sorted_list_sum([]) == []
assert sorted_list_sum(["a", "bbb", "ccccc"]) == []
assert sorted_list_sum(["aa"]) == ["aa"]
assert sorted_list_sum(["a"]) == []

# Same length strings - alphabetical sorting
assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]
assert sorted_list_sum(["ba", "aa", "ca"]) == ["aa", "ba", "ca"]

# Different even lengths
assert sorted_list_sum(["aaaa", "bb", "cccc", "dd"]) == ["bb", "dd", "aaaa", "cccc"]

# With duplicates
assert sorted_list_sum(["aa", "bb", "aa"]) == ["aa", "aa", "bb"]

# Mixed odd and even
assert sorted_list_sum(["ba", "aa", "a", "aaa", "cd"]) == ["aa", "ba", "cd"]
