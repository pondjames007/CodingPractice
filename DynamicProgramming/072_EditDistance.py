# TIPS:
# Similar to #712
#
# Recursion (TLE)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 and len(word2) == 0: return 0
        
        if len(word1) == 0: return len(word2)
        if len(word2) == 0: return len(word1)
        
        ans = 0
        if word1[-1] == word2[-1]:
            ans = self.minDistance(word1[:-1], word2[:-1])
        else:
            ans = 1 + min(self.minDistance(word1[:-1], word2), self.minDistance(word1, word2[:-1]), self.minDistance(word1[:-1], word2[:-1]))
            
        return ans

# DP
# dp[i][j] := ops to make w1[:i+1] become w2[:j+1]
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        
        dp = [[0]*(l2+1) for _ in range(l1+1)]
        
        for i in range(1, l1+1): # s2 is empty -> delete s1 -> len(s1) ops
            dp[i][0] = i
        for j in range(1, l2+1): # s1 is empty -> insert s2 -> len(s2) ops
            dp[0][j] = j
            
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if word1[i-1] == word2[j-1]: # if the last char is the same -> no ops and look for next char
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # dp[i-1][j]: delete last char from w1
                    # dp[i][j-1]: insert a char to w1 == compare w1 and w2[:-1]
                    # dp[i-1][j-1]: replace last char of w1 == delete last char of both words
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    
        return dp[-1][-1]
        


