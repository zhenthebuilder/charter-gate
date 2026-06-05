from solution import solve

# Test examples from docstring
assert solve(1000) == "1", f"Expected '1', got {solve(1000)}"
assert solve(150) == "110", f"Expected '110', got {solve(150)}"
assert solve(147) == "1100", f"Expected '1100', got {solve(147)}"

# Test edge cases
assert solve(0) == "0", f"Expected '0', got {solve(0)}"
assert solve(1) == "1", f"Expected '1', got {solve(1)}"
assert solve(10) == "1", f"Expected '1', got {solve(10)}"
assert solve(99) == "10010", f"Expected '10010', got {solve(99)}"  # 9+9=18, bin(18)='0b10010'
assert solve(10000) == "1", f"Expected '1', got {solve(10000)}"

print("All tests passed!")
