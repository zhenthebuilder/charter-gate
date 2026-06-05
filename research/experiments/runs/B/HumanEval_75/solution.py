def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def count_prime_factors(n):
        count = 0
        # Check for factor 2
        while n % 2 == 0:
            count += 1
            n //= 2
        
        # Check for odd factors from 3 onwards
        i = 3
        while i * i <= n:
            while n % i == 0:
                count += 1
                n //= i
            i += 2
        
        # If n is still > 1, then it's a prime factor
        if n > 1:
            count += 1
        
        return count
    
    return count_prime_factors(a) == 3
