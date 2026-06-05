from solution import remove_duplicates


def test_remove_duplicates():
    # Example from docstring
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
    
    # Empty list
    assert remove_duplicates([]) == []
    
    # No duplicates
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    
    # All elements are duplicates
    assert remove_duplicates([1, 1, 2, 2]) == []
    
    # Single element
    assert remove_duplicates([5]) == [5]
    
    # Multiple duplicates of same element
    assert remove_duplicates([1, 1, 1]) == []
    
    # Order preservation with mixed duplicates
    assert remove_duplicates([3, 1, 2, 1, 3, 4]) == [2, 4]


if __name__ == "__main__":
    test_remove_duplicates()
