def maxSecurityValue(security):
    n = len(security)
    
    # Memoization array to store the maximum security value for each starting node
    dp = [-1] * n
    
    def dfs(i):
        # If the result is already computed for node i, return it
        if dp[i] != -1:
            return dp[i]
        
        # Initialize the max security value starting from node i as the value at node i
        max_value = security[i]
        
        # Try jumping to all possible nodes from i
        for k in range(1, n + 1):  # k ranges from 1 to n
            next_node = i + k
            if next_node < n:
                max_value = max(max_value, security[i] + dfs(next_node))
        
        # Store the result in dp[i]
        dp[i] = max_value
        return dp[i]
    
    # Find the maximum security value starting from any node
    max_security = 0
    for i in range(n):
        max_security = max(max_security, dfs(i))
    
    return max_security

# Example usage:
security = [3, 2, 5, 10, 7]
result = maxSecurityValue(security)
print("Maximum Security Value:", result)  # Output will be 15
