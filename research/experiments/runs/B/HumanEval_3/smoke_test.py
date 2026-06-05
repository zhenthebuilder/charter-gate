from solution import below_zero


def test_below_zero():
    # Examples from docstring
    assert below_zero([1, 2, 3]) == False
    assert below_zero([1, 2, -4, 5]) == True
    
    # Extra test cases
    assert below_zero([]) == False  # Empty list
    assert below_zero([5]) == False  # Single positive deposit
    assert below_zero([-1]) == True  # Single withdrawal
    assert below_zero([10, -5, -6]) == True  # Becomes negative
    assert below_zero([1, -2, 3, -4]) == True  # Goes negative in middle
    assert below_zero([100, -50, -30, -10]) == False  # Large amounts but stays positive


if __name__ == "__main__":
    test_below_zero()
