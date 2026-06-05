def match_parens(lst):
    def is_balanced(s):
        open_count = 0
        for char in s:
            if char == '(':
                open_count += 1
            else:
                open_count -= 1
                if open_count < 0:
                    return False
        return open_count == 0
    
    if is_balanced(lst[0] + lst[1]) or is_balanced(lst[1] + lst[0]):
        return 'Yes'
    else:
        return 'No'
