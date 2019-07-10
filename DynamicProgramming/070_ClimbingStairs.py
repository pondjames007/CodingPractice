# TIPS:
# answer for n = ans for n-1 + ans for n-2

# TOP-DOWN -> RECURSIVELY
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        
        res = [-1 for i in range(n+1)]
        res[1], res[2] = 1, 2
        
        return self.dp(res, n)
    
    def dp(self, res, n):
        if n == 1: return 1
        if n == 2: return 2
        
        if res[n] == -1:
            res[n] = self.dp(res, n-1) + self.dp(res, n-2)
            
        return res[n]

# DOWN-TOP
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        
        res = [0 for i in range(n+1)]
        res[1], res[2] = 1, 2
        
        for i in range(3, n+1):
            res[i] = res[i-1] + res[i-2]
            
        return res[n]