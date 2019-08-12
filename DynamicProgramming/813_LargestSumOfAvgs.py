# TIPS
# Similar to #139, #312
# DP
# dp[k][i] := max avg of using first i elements to k groups
# need a split point j
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        sum_ = [0]*(n+1)
        dp = [[0]*(len(A)+1) for i in range(K+1)]
        
        # dp[k][i] = max avg of using first i elements to k groups
        
        for i in range(1, n+1):
            sum_[i] = sum_[i-1] + A[i-1]
            dp[1][i] = sum_[i] / i
            
        for k in range(2, K+1): # group numbers
            for i in range(k, n+1): # use how many elements, at least k elements
                for j in range(k-1, i): # split point
                    dp[k][i] = max(dp[k][i], dp[k-1][j] + (sum_[i]-sum_[j])/(i-j))
                    
        return dp[K][n]