from solution import by_length

assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
assert by_length([]) == []
assert by_length([1, -1, 55]) == ["One"]
assert by_length([5]) == ["Five"]
assert by_length([0, -1, 10, 100]) == []
assert by_length([1, 1, 1]) == ["One", "One", "One"]
assert by_length([5, 0, 3, 10, 7]) == ["Seven", "Five", "Three"]
