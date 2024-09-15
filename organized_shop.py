def getMinimumOperations(items):
    n = len(items)
    items1 = items[:]
    
    # Check the first pattern: o e o e o (odd-indexed positions are odd, even-indexed are even)
    done1 = True
    ans1 = 0
    for i in range(n):
        if i % 2 == 1:  # odd index
            while items[i] % 2 == 1:  # as long as it's odd, halve it
                items[i] //= 2
                ans1 += 1
            if items[i] % 2 == 1:  # after halving, if still odd, this pattern fails
                done1 = False
                break
        else:  # even index
            while items[i] % 2 == 0:  # as long as it's even, halve it
                items[i] //= 2
                ans1 += 1
            if items[i] % 2 == 0:  # after halving, if still even, this pattern fails
                done1 = False
                break
    
    # Check the second pattern: e o e o e (even-indexed positions are odd, odd-indexed are even)
    done2 = True
    ans2 = 0
    items = items1[:]  # Reset items back to the original
    for i in range(n):
        if i % 2 == 1:  # odd index
            while items[i] % 2 == 0:  # as long as it's even, halve it
                items[i] //= 2
                ans2 += 1
            if items[i] % 2 == 0:  # after halving, if still even, this pattern fails
                done2 = False
                break
        else:  # even index
            while items[i] % 2 == 1:  # as long as it's odd, halve it
                items[i] //= 2
                ans2 += 1
            if items[i] % 2 == 1:  # after halving, if still odd, this pattern fails
                done2 = False
                break
    
    # Determine the minimum valid answer
    ans = float('inf')
    if done1:
        ans = min(ans, ans1)
    if done2:
        ans = min(ans, ans2)
    
    return ans

# Example usage:
items = [4, 10, 10, 6, 2]
print(getMinimumOperations(items))  # Output will be 2
