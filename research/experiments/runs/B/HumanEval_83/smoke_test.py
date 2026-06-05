from solution import starts_one_ends

# Test n=1: only the number 1
assert starts_one_ends(1) == 1

# Test n=2: numbers starting with 1 (10-19) plus those ending with 1 (x1) minus overlap
# 10,11,12,...,19 (10) + 21,31,41,51,61,71,81,91 (8) + overlap 11 (already counted)
assert starts_one_ends(2) == 18

# Test n=3: 100-199 (100) + numbers ending with 1 (9*10=90) - overlap (10) = 180
assert starts_one_ends(3) == 180

# Test n=4: formula gives 18 * 10^2 = 1800
assert starts_one_ends(4) == 1800

# Test n=5: formula gives 18 * 10^3 = 18000
assert starts_one_ends(5) == 18000
