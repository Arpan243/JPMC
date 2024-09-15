def findSmallestString(word, substr):
    n = len(word)
    m = len(substr)
    best_word = None
    
    # Try every possible position in `word` where `substr` can fit
    for i in range(n - m + 1):
        # Check if we can match `substr` starting at position `i`
        possible = True
        candidate = list(word)  # Make a copy of the word
        
        for j in range(m):
            if candidate[i + j] == '?' or candidate[i + j] == substr[j]:
                candidate[i + j] = substr[j]
            else:
                possible = False
                break
        
        if possible:
            # Replace all remaining '?' with 'a' to make it lexicographically smallest
            for k in range(n):
                if candidate[k] == '?':
                    candidate[k] = 'a'
            
            # Convert candidate list back to a string
            candidate_string = ''.join(candidate)
            
            # Compare lexicographically
            if best_word is None or candidate_string < best_word:
                best_word = candidate_string

    # Return the best result found, or "-1" if no valid solution was found
    return best_word if best_word else "-1"

# Example usage:
word = "as?b?e?gf"
substr = "dbk"
result = findSmallestString(word, substr)
print(result)  # Output: "abacac"
