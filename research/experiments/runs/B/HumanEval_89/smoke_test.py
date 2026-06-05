from solution import encrypt

assert encrypt('hi') == 'lm'
assert encrypt('asdfghjkl') == 'ewhjklnop'
assert encrypt('gf') == 'kj'
assert encrypt('et') == 'ix'

assert encrypt('a') == 'e'
assert encrypt('z') == 'd'
assert encrypt('abc') == 'efg'
assert encrypt('xyz') == 'bcd'
