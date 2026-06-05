from solution import remove_vowels

def test_remove_vowels():
    # Examples from docstring
    assert remove_vowels('') == ''
    assert remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert remove_vowels('abcdef') == 'bcdf'
    assert remove_vowels('aaaaa') == ''
    assert remove_vowels('aaBAA') == 'B'
    assert remove_vowels('zbcd') == 'zbcd'
    
    # Additional cases
    assert remove_vowels('AEIOU') == ''
    assert remove_vowels('bcdfg') == 'bcdfg'
    assert remove_vowels('Hello World') == 'Hll Wrld'

if __name__ == '__main__':
    test_remove_vowels()
