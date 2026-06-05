def order_by_points(nums):
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))
    
    indexed = list(enumerate(nums))
    indexed.sort(key=lambda x: (digit_sum(x[1]), x[0]))
    return [x[1] for x in indexed]
