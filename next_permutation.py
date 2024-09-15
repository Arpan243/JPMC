def rearrange_word(word):
    # Convert the word to a list of characters (mutable)
    word_list = list(word)
    length = len(word_list)
    
    # Step 1: Find the rightmost character which is smaller than its next character
    i = length - 2
    while i >= 0 and word_list[i] >= word_list[i + 1]:
        i -= 1

    if i < 0:
        return "no answer"

    # Step 2: Find the smallest character on the right of the 'i' which is larger than word_list[i]
    j = length - 1
    while word_list[j] <= word_list[i]:
        j -= 1

    # Step 3: Swap the characters at positions i and j
    word_list[i], word_list[j] = word_list[j], word_list[i]

    # Step 4: Reverse the sequence from i+1 to end
    word_list = word_list[:i + 1] + word_list[i + 1:][::-1]

    result = ''.join(word_list)
    
    # If the result is the same as the original word, return "no answer"
    return result if result > word else "no answer"

# Example usage
word = "abdc"
print(rearrange_word(word))  # Output should be "abdc" if it's the next permutation, else "no answer"
