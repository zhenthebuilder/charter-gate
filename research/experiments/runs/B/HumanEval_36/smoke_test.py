from solution import fizz_buzz

def test_fizz_buzz():
    # From docstring examples
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
    
    # Additional test cases
    assert fizz_buzz(1) == 0
    assert fizz_buzz(77) == 0
    assert fizz_buzz(143) == 4

if __name__ == '__main__':
    test_fizz_buzz()
