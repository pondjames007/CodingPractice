# TIPS:
# Good practice to do DFS, but TLE
# DP can be the proper solution
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        ans = [float('inf')]
        
        self.lookup(A, B, 1, 0, ans)
        
        return ans[0]
    
    def lookup(self, A, B, i, count, ans):
        if count >= ans[0]: return
        
        if i == len(A):
            ans[0] = min(count, ans[0])
            return
        
        if A[i] > A[i-1] and B[i] > B[i-1]:
            self.lookup(A, B, i+1, count, ans)
            
        if A[i] > B[i-1] and B[i] > A[i-1]:
            A[i], B[i] = B[i], A[i]
            self.lookup(A, B, i+1, count+1, ans)
            A[i], B[i] = B[i], A[i]

# DP is the standard solution