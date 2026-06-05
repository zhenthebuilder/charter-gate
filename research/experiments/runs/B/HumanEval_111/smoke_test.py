from solution import histogram

assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
assert histogram('a b b a') == {'a': 2, 'b': 2}
assert histogram('a b c a b') == {'a': 2, 'b': 2}
assert histogram('b b b b a') == {'b': 4}
assert histogram('') == {}

assert histogram('a') == {'a': 1}
assert histogram('a a a') == {'a': 3}
assert histogram('x y z x y x') == {'x': 3}
assert histogram('m m m m m m m') == {'m': 7}
