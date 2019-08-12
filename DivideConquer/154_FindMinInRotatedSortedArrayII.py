# TIPS
# Use Binary Search
# Similar to #153
# when mid element == right most element, we don't know which side to choose:
# right -= 1 instead until it can choose side
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        
        while l < r:
            mid = (l+r)//2
            
            if nums[mid] < nums[r]: r = mid
            elif nums[mid] == nums[r]: r -= 1
            else: l = mid+1
                
        return nums[l]