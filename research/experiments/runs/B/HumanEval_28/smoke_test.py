from solution import concatenate


def test_concatenate():
    # Test empty list
    assert concatenate([]) == ''
    
    # Test multiple strings
    assert concatenate(['a', 'b', 'c']) == 'abc'
    
    # Test single string
    assert concatenate(['hello']) == 'hello'
    
    # Test longer list
    assert concatenate(['a', 'b', 'c', 'd', 'e']) == 'abcde'
    
    # Test strings with spaces
    assert concatenate(['hello', ' ', 'world']) == 'hello world'


if __name__ == '__main__':
    test_concatenate()
