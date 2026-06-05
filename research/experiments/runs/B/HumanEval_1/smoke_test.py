from solution import separate_paren_groups


def test_basic_example():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']


def test_empty_string():
    assert separate_paren_groups('') == []


def test_single_group():
    assert separate_paren_groups('()') == ['()']


def test_multiple_simple_groups():
    assert separate_paren_groups('()()') == ['()', '()']


def test_nested_group():
    assert separate_paren_groups('(())') == ['(())']


def test_spaces_everywhere():
    assert separate_paren_groups(' ( ( ) ) ') == ['(())']


def test_multiple_groups_with_spaces():
    assert separate_paren_groups('() ()') == ['()', '()']


def test_deeply_nested():
    assert separate_paren_groups('(((())))') == ['(((())))']


def test_alternating_pattern():
    assert separate_paren_groups('()()()') == ['()', '()', '()']


if __name__ == '__main__':
    test_basic_example()
    test_empty_string()
    test_single_group()
    test_multiple_simple_groups()
    test_nested_group()
    test_spaces_everywhere()
    test_multiple_groups_with_spaces()
    test_deeply_nested()
    test_alternating_pattern()
