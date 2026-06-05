def encode(message):
    vowel_map = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W',
    }
    
    return ''.join(
        vowel_map[char].swapcase() if char in vowel_map else char.swapcase()
        for char in message
    )
