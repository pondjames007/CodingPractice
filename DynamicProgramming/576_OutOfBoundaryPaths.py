# TIPS:
#
# DP
# dp[k][i][j] := no. of pathsa to point (i, j) on k-th step
# expand the grid with one 'outer circle' to represent out of boundary
# dim. of dp = (N+1, m+2, n+2)
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        if N == 0: return 0
        
        dp = [[[0]*(n+2) for _ in range(m+2)] for _ in range(N+1)]
        dp[0][i+1][j+1] = 1
        ans = 0
        for k in range(1, N+1):
            for a in range(m+2):
                for b in range(n+2):
                    if a > 1 and (b != 0 and b != n+1):
                        dp[k][a][b] += dp[k-1][a-1][b]
                    if a < m and (b != 0 and b != n+1):
                        dp[k][a][b] += dp[k-1][a+1][b]
                    if b > 1 and (a != 0 and a != m+1):
                        dp[k][a][b] += dp[k-1][a][b-1]
                    if b < n and (a != 0 and a != m+1):
                        dp[k][a][b] += dp[k-1][a][b+1]
                    if a == 0 or a == m+1 or b == 0 or b == n+1:
                        ans += dp[k][a][b]
        return ans%(10**9+7)
                