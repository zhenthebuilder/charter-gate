def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest = -1
    
    # Handle factor 2
    while n % 2 == 0:
        largest = 2
        n = n // 2
    
    # Handle odd factors from 3 onwards
    i = 3
    while i * i <= n:
        while n % i == 0:
            largest = i
            n = n // i
        i += 2
    
    # If n is still greater than 1, then it's a prime factor
    if n > 1:
        largest = n
    
    return largest
