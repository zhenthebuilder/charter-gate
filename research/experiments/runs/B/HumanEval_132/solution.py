def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    open_positions = [i for i, c in enumerate(string) if c == '[']
    close_positions = [i for i, c in enumerate(string) if c == ']']

    if len(open_positions) < 2 or len(close_positions) < 2:
        return False

    return open_positions[1] < close_positions[-2]
