from solution import make_palindrome

def test_empty_string():
    assert make_palindrome('') == ''

def test_single_char():
    assert make_palindrome('a') == 'a'

def test_cat():
    assert make_palindrome('cat') == 'catac'

def test_cata():
    assert make_palindrome('cata') == 'catac'

def test_already_palindrome():
    assert make_palindrome('aba') == 'aba'
    assert make_palindrome('racecar') == 'racecar'

def test_two_chars():
    assert make_palindrome('ab') == 'aba'

def test_longer_string():
    assert make_palindrome('abcd') == 'abcdcba'

if __name__ == '__main__':
    test_empty_string()
    test_single_char()
    test_cat()
    test_cata()
    test_already_palindrome()
    test_two_chars()
    test_longer_string()
