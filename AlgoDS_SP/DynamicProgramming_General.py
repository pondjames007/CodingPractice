# DP
def dp():
    dp = ...                # Create DP array
                            # add padding if needed (usually we need it and our data start from 1)
    dp[0][0] = ...          # init dp array
                            # best case
    for i ...:
        for j ...:
            ...
            dp[i][j] = ...  # transition
    
    return dp[n][m]


# Recursion with Memoization:
    mem = ...                           # create mem dict
    def dp(i, j, ...):
        if base_case(i, j): return ...  # base_case
        if (i, j) not in mem:
            mem[i, j] = ...             # transition
        return mem[(i, j)]

    return dp(n, m)

    