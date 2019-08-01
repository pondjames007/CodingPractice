# TIPS:
# enumerate 2**l and find out if bit i is 1 -> nums[i] is in the subset
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        ans = []
        
        for s in range(2**l):
            tmp = []
            for i in range(l):
                if s & 1 << i: tmp.append(nums[i])
                    
            ans.append(tmp)
        
        return ans