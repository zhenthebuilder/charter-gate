import re

def is_bored(S):
    sentences = re.split(r'[.?!]', S)
    
    count = 0
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence and re.match(r'^I\b', sentence):
            count += 1
    
    return count
