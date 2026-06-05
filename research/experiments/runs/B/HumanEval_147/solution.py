def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
    For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
    Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    # a[i] % 3 depends on i % 3:
    # i % 3 == 0 or 1 => a[i] % 3 == 1
    # i % 3 == 2 => a[i] % 3 == 0
    
    count0 = (n + 1) // 3  # Count where i % 3 == 2
    count1 = n - count0     # Count where i % 3 == 0 or 1
    
    # Triples sum to 0 (mod 3) when all three have same remainder
    def comb_3(k):
        if k < 3:
            return 0
        return k * (k - 1) * (k - 2) // 6
    
    return comb_3(count0) + comb_3(count1)
