from solution import all_prefixes


def test_all_prefixes():
    # Example from docstring
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    
    # Empty string
    assert all_prefixes('') == []
    
    # Single character
    assert all_prefixes('a') == ['a']
    
    # Longer string
    assert all_prefixes('hello') == ['h', 'he', 'hel', 'hell', 'hello']
    
    # Two characters
    assert all_prefixes('ab') == ['a', 'ab']


if __name__ == '__main__':
    test_all_prefixes()
