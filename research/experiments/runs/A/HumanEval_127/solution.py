def intersection(interval1, interval2):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    
    if start > end:
        return "NO"
    
    length = end - start
    
    return "YES" if is_prime(length) else "NO"
