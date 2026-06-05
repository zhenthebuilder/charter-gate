def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if n == 1:
        return x == 1
    if n == 0:
        return x in (1, 0)
    if n == -1:
        return x in (1, -1)
    
    power = 1
    if abs(n) > 1:
        while abs(power) <= abs(x):
            if power == x:
                return True
            power *= n
    
    return False
