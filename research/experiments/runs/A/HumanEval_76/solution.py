def is_simple_power(x, n):
    # n = 1: only 1^k = 1 for all k
    if n == 1:
        return x == 1
    
    # n = 0: 0^0 is convention defined as 1
    if n == 0:
        return x == 1
    
    # n = -1: (-1)^k is either 1 or -1
    if n == -1:
        return x in [1, -1]
    
    # For positive n > 1, x must be positive
    if n > 1 and x <= 0:
        return False
    
    # x = 1: n^0 = 1 for any n != 0
    if x == 1:
        return True
    
    # For |n| > 1: repeatedly divide x by n
    while True:
        if x % n != 0:
            return False
        x = x // n
        if x == 1:
            return True
