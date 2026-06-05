from solution import words_string

def test_words_string():
    # Test cases from docstring
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
    # Additional test cases
    assert words_string("a b c") == ["a", "b", "c"]
    assert words_string("a,b,c") == ["a", "b", "c"]
    assert words_string("a, b, c") == ["a", "b", "c"]
    assert words_string("hello world") == ["hello", "world"]
    assert words_string("one") == ["one"]
    assert words_string("a  b  c") == ["a", "b", "c"]

if __name__ == "__main__":
    test_words_string()
