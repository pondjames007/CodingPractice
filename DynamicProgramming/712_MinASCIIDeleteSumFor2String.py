# TIPS:
# Similar to #072
#
# Recursion with Memoization: (SLOW when recursive depth is too deep)
# delete the last char, if A[-1] == B[-1] -> cost = 0 else cost = min(A[-1], B[-1])
# calc the cost to make both strings empty
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1 = len(s1)
        l2 = len(s2)
        mem = [[-1]*(l2+1) for _ in range(l1+1)]
        
        return self.dp(s1, l1, s2, l2, mem)
    
    def dp(self, s1, i, s2, j, mem):
        if i == 0 and j == 0: return 0
        if mem[i][j] >= 0: return mem[i][j] # if calculated
        if i == 0: # s1 is empty
            mem[i][j] = self.dp(s1, i, s2, j-1, mem) + ord(s2[j-1])
            return mem[i][j]
        if j == 0: # s2 is empty
            mem[i][j] = self.dp(s1, i-1, s2, j, mem) + ord(s1[i-1])
            return mem[i][j]
        
        if s1[i-1] == s2[j-1]: # s1[-1] == s2[-1], cost == 0
            mem[i][j] = self.dp(s1, i-1, s2, j-1, mem)
            return mem[i][j]
        
        # delete s1[-1] or s2[-1] see which cost less
        mem[i][j] = min(self.dp(s1, i-1, s2, j, mem) + ord(s1[i-1]), self.dp(s1, i, s2, j-1, mem) + ord(s2[j-1]))
        return mem[i][j]


# DP
# dp[i][j] := min delete sum of s1[0:i], s2[0:j]
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1 = len(s1)
        l2 = len(s2)
        dp = [[0]*(l2+1) for _ in range(l1+1)]
        
        for i in range(1, l1+1): # init.: if s2 is empty
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, l2+1): # init.: if s1 is empty
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
            
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if s1[i-1] == s2[j-1]: # keep s1[i-1] and s2[j-1]
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        return dp[l1][l2]