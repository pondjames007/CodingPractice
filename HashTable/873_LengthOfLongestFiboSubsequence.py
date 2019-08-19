# TIPS:
#
# Sol1: DP
# dp[i][j] := max len of seq ends with A[i], A[j]
# Init: dp[i][j] = all to 2 (invalid)
# dp[j][k] = dp[i][j] + 1
# where i < j < k and A[i] + A[j] = A[k] and check A[k] - A[j] in A
# T: O(n^2)
# S: O(n^2)
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        dic = {} # use hash table to efficiently find out whether A[k]-A[j] is in A
        for i in range(n):
            dic[A[i]] = i
            
        dp = [[2]*n for _ in range(n)]
        ans = 0
        for j in range(n):
            for k in range(j, n):
                a_i = A[k] - A[j]
                if a_i >= A[j]: break # since A[k] will be larger next round, we don't need to check to the end of A
                if a_i not in dic: continue
                
                i = dic[a_i]
                dp[j][k] = dp[i][j] + 1
                ans = max(ans, dp[j][k])
        
        return ans 


# Sol2: Hash Table
# For each pair A[i], A[j], generate a Fib Seq
# check whether each element is in A or not
# T: O(n^3), but practically it is near O(n^2) it is easy to break
# S: O(n) 
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        dic = set(A)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                a = A[i]
                b = A[j]
                c = a + b
                l = 2
                while c in dic:
                    a = b
                    b = c
                    c = a + b
                    l += 1
                    ans = max(ans, l)
                    
        return ans