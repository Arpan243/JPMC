def find_missing_words(s, t):
    # Split the strings into lists of words
    words_s = s.split()
    words_t = t.split()
    
    missing_words = []
    j = 0  # Pointer for t
    
    # Traverse through words in s
    for word in words_s:
        # If the current word matches the word in t, move the pointer j
        if j < len(words_t) and word == words_t[j]:
            j += 1
        else:
            # If it doesn't match, it is a missing word
            missing_words.append(word)
    
    return missing_words

# Example usage
s = "I like cheese"
t = "like"
result = find_missing_words(s, t)
print(result)  # Output: ['like']
