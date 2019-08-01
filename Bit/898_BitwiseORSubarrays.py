# TIPS:
#
# Medium but HARD
# 1. Brute Force (TLE)
# 2. DP (TLE)
#    dp[i][j] = A[i] | ... | A[j]
#    dp[i][j] = dp[i][j-1] | A[j]
class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0]*n for _ in range(n)]
        ans = set(A)
        
        for l in range(1, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if l == 1:
                    dp[i][j] = A[i]
                    continue
                dp[i][j] = dp[i][j-1] | A[j]
                ans.add(dp[i][j])
                
        return len(ans)
        

# 3. DP compressed
# dp has too many overlapped element
# dp[i] := bitwise ORs of all subarrays end with A[i]
# dp[i] = [b | A[i] for b in dp[i-1]] + A[i]
# len(dp[i]) <= 32
class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        n = len(A)
        ans = set()
        cur = set()
        nxt = set()
        
        for a in A:
            nxt.clear()
            nxt.add(a)
            for b in cur:
                nxt.add(a | b)
            cur, nxt = nxt, cur
            
            ans |= cur
        return len(ans)
        