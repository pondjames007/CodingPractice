# TIPS:

# Math Solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0: return 0
        if m == 1 or n == 1: return 1
        
        m -= 1
        n -= 1
        ans = int(self.factorial(m+n)/(self.factorial(m)*self.factorial(n)))
        
        return ans
    
    def factorial(self, n):
        
        ans = 1
        for i in range(1,n+1):
            ans *= i
            
        return ans

# DP
# dp[i][j] := possible num of paths to point (i, j)
# dp[i][j] = dp[i-1][j] + dp[i][j-1]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: dp[i][j] = 1
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
                    
        return dp[-1][-1]