# TIPS
#
# DP
# similar to #062
# add a condition to see if the point has obstacle or not
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1: return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: 
                    dp[i][j] = 1
                    continue
                if obstacleGrid[i][j] == 1: continue
                
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
                    
        
        return dp[m-1][n-1]
                