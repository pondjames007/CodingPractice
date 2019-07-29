# 1.1 Input O(n)
# dp[i] only depends on first i elements, but only **constant** number
# Time:  O(n)
# Space: O(n) -> O(1) 
def dp_1_1():
    dp = [0] * n+1                      # init dp array
    for i in range(1, n):               # problem size
        dp[i] = f(dp[i-1], dp[i-2], ...)# depends on how many previous problems

    return dp[n]

# 1.2 Input O(n)
# dp[i] depends on all first i elements, and find the best one from it
# Time:  O(n^2)
# Space: O(n)
def dp_1_2():
    dp = [0] * n+1                      # init dp array
    for i = range(1, n):                # problem size
        for j in range(1, i-1):         # sub-problem size (cannot larger than main problem size)
            dp[i] = max(dp[i], f(dp[j]))# the optimal answer will be chosen from the answers among sub-problems

    return dp[n]

# 1.3 Input O(n) + O(m)
# 2 inputs (arrays/strings)
# dp[i][j] depends on constant previous sub-problems
# Time:  O(mn)
# Space: O(mn) 
def dp_1_3():
    dp = [[0] * n for _ in range(m)]     # init dp array
    for i in range(1, n):                # problem size of input 1
        for j in range(1, m):            # problem size of input 2
            dp[i][j] = f(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

    return dp[n][m]

# 1.4 Input O(n)
# dp[i] depends on previous sub-problems
# but each sub-problem depends on other O(n) sub-sub-problems
# Time:  O(n^3)
# Space: O(n^2) 
def dp_1_4():
    dp = [[0] * n for _ in range(m)]    # init 2D array
    for l in range(1, n):               # problem size
        for i in range(1, n-l):         # sub-problem start
            j = i+l-1                   # sub-problem end
            for k in range(i, j):       # try all possible break points
                dp[i][j] = max(dp[i][j], f(dp[i][k], dp[k][j])) # merge 2 sub-problems
    return dp[1][n]

# 2.1 Input O(mn)
# 1 input (2D Array/Matrix)
# dp[i][j] depends on constsant sub-problems
# Time:  O(mn)
# Space: O(mn) -> O(m) 
def dp_2_1():
    dp = [[0] * n for _ in range(m)]    # init 2D array
    for i in range(1, n):               # row: top -> bottom
        for j in range(1, m):           # col: left -> right
            dp[i][j] = f(dp[i-1][j], dp[i][j-1])

    return dp[n][m] # or max(dp[n])

# 2.2 Input O(mn)
# dp[k][i][j] depends on constant sub-problems
# Time:  O(kmn)
# Space: O(kmn) -> O(mn)
def dp_2_2():
    dp = [[[0] * n for _ in range(m)] for _ in range(K)]
    for k in range(1, K):
        for i in range(1, n):
            for j in range(1, m):
                dp[k][i][j] = f(dp[k-1][i+di][j+dj])
    return dp[K][n][m] # or g(dp[k])
