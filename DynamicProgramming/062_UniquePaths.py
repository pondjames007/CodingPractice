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

