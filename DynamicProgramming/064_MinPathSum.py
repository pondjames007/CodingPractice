# TIPS:
# 
# DP
# similar to #063, #062
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[float('Inf')]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: dp[i][j] = grid[0][0]
                    
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])
                
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])
                    
        return dp[m-1][n-1]

# DP
# do some initialization will be faster
# or maybe it is because I didn't make a new dp array
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        
        m = len(grid)
        n = len(grid[0])
        
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    
                    
        return grid[-1][-1]