# TIPS:
#
# idx = i*c + j
# original = (idx//o_c, idx%o_c)
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        o_r = len(nums)
        o_c = len(nums[0])
        
        if r <= 0 or c <= 0 or r*c != o_r*o_c: return nums
        
        ans = [[0]*c for _ in range(r)]
        
        for i in range(r):
            for j in range(c):
                idx = i*c+j
                ans[i][j] = nums[idx//o_c][idx%o_c]
                
        return ans