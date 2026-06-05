def any_int(x, y, z):
    def is_integer(n):
        if isinstance(n, bool):
            return False
        if isinstance(n, int):
            return True
        if isinstance(n, float):
            return n == int(n)
        return False
    
    if not (is_integer(x) and is_integer(y) and is_integer(z)):
        return False
    
    return (x == y + z) or (y == x + z) or (z == x + y)
