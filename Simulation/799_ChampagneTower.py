# TIPS:
#
# DP
# dp[i][j] := cumulative amount
# dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0]*(query_row+2) for _ in range(query_row+1)]
        dp[0][1] = poured
        
        for i in range(1, query_row+1):
            for j in range(1, query_row+2):
                a = dp[i-1][j] - 1 if dp[i-1][j] > 1 else 0
                b = dp[i-1][j-1] - 1 if dp[i-1][j-1] > 1 else 0
                dp[i][j] = (a + b)/2
                if dp[i][j] < 0: dp[i][j] = 0 
                
        return dp[query_row][query_glass+1] if dp[query_row][query_glass+1] < 1 else 1