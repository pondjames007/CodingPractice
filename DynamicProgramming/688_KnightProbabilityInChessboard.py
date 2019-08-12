# TIPS:
#
# DP
# dp[k][i][j] := possiblity of stopping at (i, j) on k-th step
# dp[k][i][j] = dp[k-1][a][b] where a and b are possible points walk from (8 possible points)
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0: return 1.0
        
        dp = [[[0]*N for _ in range(N)] for _ in range(K+1)]
        dp[0][r][c] = 1
        
        for k in range(1, K+1):
            for i in range(N):
                for j in range(N):
                    if i >= 2 and j >= 1: dp[k][i][j] += dp[k-1][i-2][j-1]
                    if i >= 2 and j < N-1: dp[k][i][j] += dp[k-1][i-2][j+1]
                    if i >= 1 and j >= 2: dp[k][i][j] += dp[k-1][i-1][j-2]
                    if i >= 1 and j < N-2: dp[k][i][j] += dp[k-1][i-1][j+2]
                    if i < N-1 and j >= 2: dp[k][i][j] += dp[k-1][i+1][j-2]
                    if i < N-1 and j < N-2: dp[k][i][j] += dp[k-1][i+1][j+2]
                    if i < N-2 and j >= 1: dp[k][i][j] += dp[k-1][i+2][j-1]
                    if i < N-2 and j < N-1: dp[k][i][j] += dp[k-1][i+2][j+1]
                    
                    dp[k][i][j] /= 8
                    
        return sum([sum(dp[K][i]) for i in range(N)])