def min_cost_to_equalize(arr):
    cost = 0
    for i in range(1, len(arr)):
        # Calculate the difference between current and previous element
        diff = arr[i] - arr[i-1]
        
        # If they are different, apply the operation to the prefix
        if diff != 0:
            cost += abs(diff)
    
    return cost

# Example usage:
arr = [1, 2, 1, 5]
print(min_cost_to_equalize(arr))  # Output will be 6
