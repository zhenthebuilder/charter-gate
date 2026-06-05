from solution import select_words

def test_select_words():
    # From docstring examples
    assert select_words("Mary had a little lamb", 4) == ["little"]
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert select_words("simple white space", 2) == []
    assert select_words("Hello world", 4) == ["world"]
    assert select_words("Uncle sam", 3) == ["Uncle"]
    
    # Edge cases
    assert select_words("", 0) == []
    assert select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]
    assert select_words("b c d", 1) == ["b", "c", "d"]
    assert select_words("aeiou", 0) == ["aeiou"]
    assert select_words("xyz", 3) == ["xyz"]

if __name__ == "__main__":
    test_select_words()
