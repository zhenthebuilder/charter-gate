from solution import sort_numbers

# Docstring example
assert sort_numbers('three one five') == 'one three five'

# Single number
assert sort_numbers('five') == 'five'

# Already sorted
assert sort_numbers('one two three') == 'one two three'

# Reverse sorted
assert sort_numbers('nine eight seven') == 'seven eight nine'

# Duplicates
assert sort_numbers('five five five') == 'five five five'

# All digits
assert sort_numbers('zero one two three four five six seven eight nine') == 'zero one two three four five six seven eight nine'

# Random order
assert sort_numbers('nine two zero five eight') == 'zero two five eight nine'
