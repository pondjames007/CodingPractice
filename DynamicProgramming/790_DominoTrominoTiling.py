# TIPS:
#
# When only rectangle domino, the answer will become a Fibonacci Sequence
# dp[i][0] = ways to cover i cols, both rows of col i are covered.
# dp[i][1] = ways to cover i cols, only top row of col i is covered.
# dp[i][2] = ways to cover i cols, only bottom row of col i is covered. 
# 
# dp[i][0] = dp[i-1][0] + dp[i-2][0] + dp[i-1][1] + dp[i-1][2]
# dp[i][1] = dp[i-2][0] + dp[i-1][2]
# dp[i][2] = dp[i-2][0] + dp[i-1][1]
# 
# dp[i][1] == dp[i][2] is always true

class Solution:
    def numTilings(self, N: int) -> int:
        kmod = 10**9 + 7
        dp = [[0,0] for _ in range(N+1)]
        dp[0][0] = dp[1][0] = 1
        
        for i in range(2, N+1):
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + 2*dp[i-1][1]) % kmod
            dp[i][1] = (dp[i-2][0] + dp[i-1][1]) % kmod
            
        
        return dp[N][0]