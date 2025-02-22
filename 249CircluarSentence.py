def isCircularSentence(sentence: str) -> bool:
    words = sentence.split()
    n = len(words)
    
    # Check if the last character of each word matches the first character of the next word
    for i in range(n):
        current_word = words[i]
        next_word = words[(i + 1) % n]  # Use modulo to wrap around to the first word
        
        if current_word[-1] != next_word[0]:
            return False
    
    return True

# Test the function
print(isCircularSentence("leetcode exercises sound delightful"))  # Output: True
print(isCircularSentence("eetcode"))  # Output: True
print(isCircularSentence("Leetcode is cool")) # Output: False
print(isCircularSentence("Leetcode cool")) # Output: False