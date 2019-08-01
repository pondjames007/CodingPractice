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
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        keep = [float('inf')]*n
        swap = [float('inf')]*n
        keep[0] = 0
        swap[0] = 1
        
        for i in range(1, n):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                # Good Case: No Swap NEEDED
                keep[i] = keep[i-1]
                # Swapped i-1, so you should swap i too
                swap[i] = swap[i-1] + 1
            
            if A[i] > B[i-1] and B[i] > A[i-1]:
                # swapped i-1, no need to swap i
                keep[i] = min(keep[i], swap[i-1]) 
                # i-1 not swapped
                swap[i] = min(swap[i], keep[i-1] + 1)
                
        return min(keep[-1], swap[-1])