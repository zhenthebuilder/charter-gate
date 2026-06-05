def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    min_val = min(a, b)
    max_val = max(a, b)
    
    return [d for d in [0, 2, 4, 6, 8] if min_val <= d <= max_val]
