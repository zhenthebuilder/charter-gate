from solution import Strongest_Extension

# Docstring example 1
assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

# Docstring example 2
assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

# Tie-breaking: same strength, pick first
assert Strongest_Extension('Test', ['AAA', 'BBB']) == 'Test.AAA'

# Single extension
assert Strongest_Extension('Single', ['MyExt']) == 'Single.MyExt'

# Negative strengths
assert Strongest_Extension('Negative', ['aaa', 'bb', 'c']) == 'Negative.c'

# All lowercase
assert Strongest_Extension('AllLower', ['abc', 'def']) == 'AllLower.abc'
