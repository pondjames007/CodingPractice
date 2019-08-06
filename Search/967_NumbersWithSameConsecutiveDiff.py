# TIPS:
# Use DFS

class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        ans = []
        
        if N == 1: return [i for i in range(10)]
        
        for i in range(1, 10):
            ans += self.lookup(N, K, str(i), 1)
            
        return ans
    
    def lookup(self, N, K, num, digits):
        if digits == N: return [int(num)]
        
        res = []
        for i in range(10):
            if abs(i - int(num[-1])) == K:
                res += self.lookup(N, K, num + str(i), digits+1)
                
        return res