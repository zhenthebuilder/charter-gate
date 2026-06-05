from solution import modp

def test_modp():
    # Examples from docstring
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1
    
    # Additional test cases
    assert modp(0, 5) == 1  # 2^0 = 1
    assert modp(1, 5) == 2  # 2^1 = 2
    assert modp(2, 5) == 4  # 2^2 = 4
    assert modp(4, 5) == 1  # 2^4 = 16, 16 % 5 = 1
    assert modp(5, 7) == 4  # 2^5 = 32, 32 % 7 = 4
    assert modp(10, 1009) == pow(2, 10, 1009)  # Larger values

if __name__ == "__main__":
    test_modp()
