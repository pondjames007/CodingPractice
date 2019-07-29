# TIPS:

# DP (Similar to #818)
# dp[i][0] := ans of S[0:i+1] and S[i] = 0 -> total steps to make first i digits are all 0
# dp[i][1] := ans of S[0:i+1] and S[i] = 1 -> total steps to make the last digit equals 1 (all digits after i should all be 1)
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n = len(S)
        dp = [[0, 0] for _ in range(n+1)]
        S = list(S)
        
        for i in range(1, n+1):
            if S[i-1] == '0':   # dp有多一位 所以S要i-1
                dp[i][0] = dp[i-1][0]
                dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1
            else:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = min(dp[i-1][0], dp[i-1][1])
                
        return min(dp[-1][0], dp[-1][1])


# DP (Prefix + Suffix)
# l[i] := # of min flips -> S[0] ~ S[i] are all 0
# r[i] := # of min flips -> S[i] ~ S[n-1] are all 1
# ans = min(l[i-1] + r[i], l[n-1], r[0])
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n = len(S)
        
        l = [0]*(n+1) # 1 -> 0
        r = [0]*(n+1) # 0 -> 1
        
        l[0] = 0 if S[0] == '0' else 1
        r[n-1] = 0 if S[n-1] == '1' else 1
        
        for i in range(1, n):
            c = 0 if S[i] == '0' else 1
            l[i] = l[i-1] + c
        for i in range(n-2, -1, -1):
            c = 0 if S[i] == '1' else 1
            r[i] = r[i+1] + c
        
        ans = r[0]
        for i in range(1, n+1):
            ans = min(ans, l[i-1] + r[i])
            
        return ans