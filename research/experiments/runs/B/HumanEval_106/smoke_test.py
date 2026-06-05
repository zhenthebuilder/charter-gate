from solution import f

def test():
    # Test the given example
    assert f(5) == [1, 2, 6, 24, 15]
    
    # Test edge cases
    assert f(1) == [1]
    assert f(2) == [1, 2]
    assert f(3) == [1, 2, 6]
    assert f(4) == [1, 2, 6, 24]
    assert f(6) == [1, 2, 6, 24, 15, 720]

if __name__ == '__main__':
    test()
