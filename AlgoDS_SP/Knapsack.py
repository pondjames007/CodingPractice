# General 0-1 Knapsack DP solution
def Knapsack01(N, W, w, v): # No. objects, goal weight, weight list, value list
    dp = [[0]*(N+1) for _ in range(W+1)]
    for i in range(1, N+1):
        for j in range(W+1):
            dp[i][j] = max(dp[i][j], dp[i-1][j-w[i]] + v[i])

    return max(dp[N])

# Use tmp Array to reduce dimension
def Knapsack01_tmpArr(N, W, w, v):
    dp = [0]*(W+1)
    for i in range(1, N+1):
        tmp = [0]*(W+1)
        for j in range(w[i], W+1):
            tmp[j] = max(tmp[j], dp[j-w[i]] + v[i])

    dp = tmp
    return max(dp)

# Use Iterator j in reverse order to reduce dimension
# Reverse Order prevents object i being used multiple times
def Knapsack01_reverse_push(N, W, w, v):
    dp = [0]*(W+1) 
    for i in range(1, N+1):
        for j in range(W-w[i], -1):
            dp[j+w[i]] = max(dp[j+w[i]], dp[j]+v[i])

    return max(dp)

def Knapsack01_reverse_pull(N, W, w, v):
    dp = [0]*(W+1) 
    for i in range(1, N+1):
        for j in range(W, w[i]-1):
            dp[j+w[i]] = max(dp[j+w[i]], dp[j]+v[i])

    return max(dp)


# Unbound Knapsack Problem
# Every Item can use Unlimited times

# Sol1: reduce to 0-1 Knapsack Problem (Naive)
# Expand the item list, each item appears lower(W/w[i]) times

# Sol2: reduce to 0-1 Knapsack Problem (Better)
# Assume the optimal solution uses m objects, and m is the combination of 2^k
# Expand the item list:
#    (w[i], v[i]) -> {(w[i], v[i]), (2w[i], 2v[i]), ..., (2^k*w[i], 2^k*v[i])}
def KnapsackComplete_Reduce(N, W, w, v):
    for i in range(1, N+1):
        for k in range(math.log(W/w[i])):
            Knapsack01(N, W, w[i]<<k, v[i]<<k)


# Sol3: Use each item more than once more efficiently
# Iterate j in NORMAL order
def KnapsackComplete(N, W, w, v):
    for i in range(1, N+1):
        for j in range(w, W+1):
            dp[j] = max(dp[j], dp[j-w[i]]+v[i])


# Bounded Knapsack Problem
# Every Item is limited to use n[i] times

# Sol1: reduce to 0-1 Knapsack Problem (Naive)

# Sol2: reduce to 0-1 Knapsack Problem (Better)
# if n[i] * w[i] >= W => reduce to Complete Knapsack
#
# Assume the optimal solution object i use m <= n[i] times
# m will be the combination of 2^(k-1), k < log(n[i]) and n[i] >= 2^k + 1
def Knapsack_Bound(N, W, w, v, n):
    for i in range(1, N+1):
        if n[i] * w[i] >= W:
            KnapsackComplete(N, W, w[i], v[i])
            continue
        left = n[i]
        for k in range(math.log(n[i])):
            Knapsack01(N, W, w[i]<<k, v[i]<<k)
            left -= 1<<k
        Knapsack01(N, W, w[i]*left, v[i]*left)