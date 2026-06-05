from solution import intersperse


def test_intersperse():
    # Test empty list
    assert intersperse([], 4) == []
    
    # Test single element
    assert intersperse([1], 4) == [1]
    
    # Test docstring example
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    
    # Test with two elements
    assert intersperse([1, 2], 4) == [1, 4, 2]
    
    # Test with delimiter 0
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    
    # Test with negative numbers
    assert intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]


if __name__ == "__main__":
    test_intersperse()
