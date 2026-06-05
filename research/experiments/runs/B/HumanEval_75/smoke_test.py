from solution import is_multiply_prime

# From docstring example
assert is_multiply_prime(30) == True, "30 = 2 * 3 * 5"

# Other valid cases (product of exactly 3 primes)
assert is_multiply_prime(8) == True, "8 = 2 * 2 * 2"
assert is_multiply_prime(12) == True, "12 = 2 * 2 * 3"
assert is_multiply_prime(18) == True, "18 = 2 * 3 * 3"
assert is_multiply_prime(27) == True, "27 = 3 * 3 * 3"
assert is_multiply_prime(50) == True, "50 = 2 * 5 * 5"

# Invalid cases
assert is_multiply_prime(6) == False, "6 = 2 * 3 (only 2 prime factors)"
assert is_multiply_prime(2) == False, "2 (only 1 prime factor)"
assert is_multiply_prime(1) == False, "1 (no prime factors)"
assert is_multiply_prime(4) == False, "4 = 2 * 2 (only 2 prime factors)"
assert is_multiply_prime(5) == False, "5 (only 1 prime factor)"
assert is_multiply_prime(24) == False, "24 = 2 * 2 * 2 * 3 (4 prime factors)"

# Edge cases
assert is_multiply_prime(99) == True, "99 = 3 * 3 * 11"
assert is_multiply_prime(98) == True, "98 = 2 * 7 * 7"
