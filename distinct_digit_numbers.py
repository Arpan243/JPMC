dp = [[[[-1 for _ in range(2)] for _ in range(1 << 10)] for _ in range(2)] for _ in range(11)]

def memset(dp):
    for i in range(11):
        for j in range(2):
            for k in range(1 << 10):
                for l in range(2):
                    dp[i][j][k][l] = -1

def recur(i, j, k, l, a):
    if i == len(a):
        return 1
    if dp[i][j][k][l] != -1:
        return dp[i][j][k][l]
    
    ans = 0
    
    if j == 1:
        for digit in range(10):
            mask = (1 << digit)
            if mask & k:
                if digit == int(a[i]):
                    ans += recur(i + 1, 1, k - (1 << digit), 1, a)
                elif digit == 0:
                    ans += recur(i + 1, 0, k, 0, a)
                elif digit < int(a[i]):
                    ans += recur(i + 1, 0, k - (1 << digit), 1, a)
    else:
        for digit in range(10):
            mask = (1 << digit)
            if mask & k:
                if digit == 0 and l == 0:
                    ans += recur(i + 1, 0, k, 0, a)
                elif digit == 0 and l == 1:
                    ans += recur(i + 1, 0, k - (1 << digit), 1, a)
                else:
                    ans += recur(i + 1, 0, k - (1 << digit), 1, a)
    
    dp[i][j][k][l] = ans
    return ans

def countInRange(A, B):
    memset(dp)
    A -= 1
    L = str(A)
    R = str(B)
    ans1 = recur(0, 1, (1 << 10) - 1, 0, L)
    memset(dp)
    ans2 = recur(0, 1, (1 << 10) - 1, 0, R)
    return ans2 - ans1

def handleQueries(queries):
    results = []
    for L, R in queries:
        results.append(countInRange(L, R))
    return results

# Example usage
queries = [(1, 20), (9, 19), (50, 500)]
print(handleQueries(queries))
