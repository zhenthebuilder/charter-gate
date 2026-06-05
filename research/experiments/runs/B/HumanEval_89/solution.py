def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            shifted = (ord(char) - ord('a') + 4) % 26
            result.append(chr(ord('a') + shifted))
        elif 'A' <= char <= 'Z':
            shifted = (ord(char) - ord('A') + 4) % 26
            result.append(chr(ord('A') + shifted))
        else:
            result.append(char)
    return ''.join(result)
