def find_max(words):
    if not words:
        return ""
    
    max_unique = max(len(set(word)) for word in words)
    candidates = [word for word in words if len(set(word)) == max_unique]
    return min(candidates)
