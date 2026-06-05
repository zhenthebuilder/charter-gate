from solution import rolling_max


def test_rolling_max():
    # Example from docstring
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
    
    # Single element
    assert rolling_max([5]) == [5]
    
    # Empty list
    assert rolling_max([]) == []
    
    # All increasing
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # All decreasing
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]
    
    # All same
    assert rolling_max([3, 3, 3, 3]) == [3, 3, 3, 3]
    
    # Negative numbers
    assert rolling_max([-5, -3, -4, -1]) == [-5, -3, -3, -1]


if __name__ == "__main__":
    test_rolling_max()
