from solution import maximum

def test_maximum():
    # Example 1
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
    
    # Example 2
    assert maximum([4, -4, 4], 2) == [4, 4]
    
    # Example 3
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
    
    # Edge case: k = 0
    assert maximum([1, 2, 3], 0) == []
    
    # Edge case: k = len(arr)
    assert maximum([1], 1) == [1]
    
    # Negative numbers only
    assert maximum([-5, -3, -1], 2) == [-3, -1]
    
    # Duplicates
    assert maximum([1, 1, 1], 2) == [1, 1]
    
    # Single element with k=1
    assert maximum([42], 1) == [42]
    
    # Mixed positive and negative
    assert maximum([-10, 5, 0, 15, -5], 3) == [0, 5, 15]

if __name__ == "__main__":
    test_maximum()
