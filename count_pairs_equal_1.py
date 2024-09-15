from collections import defaultdict

def count_pairs_with_same_ones(arr):
    # Function to count the number of 1's in the binary representation
    def count_ones(n):
        return bin(n).count('1')
    
    # Dictionary to store the count of numbers having the same number of 1's
    count_map = defaultdict(int)
    
    # Count how many numbers have the same count of 1's
    for num in arr:
        ones_count = count_ones(num)
        count_map[ones_count] += 1
    
    # Now count the number of valid pairs
    total_pairs = 0
    for count in count_map.values():
        if count > 1:
            total_pairs += (count * (count - 1)) // 2
    
    return total_pairs

# Example usage
arr = [5, 3, 7, 10]
print(count_pairs_with_same_ones(arr))  # Output will be 1
