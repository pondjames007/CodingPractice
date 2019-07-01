# TIPS:
# sort the array
# if nums[-1](max) > 0:
#   nums[-1] & (nums[0] & nums[1]) or nums & nums[2] & nums[3]
# if nums[-1] <= 0: 
#   nums[0] & nums[1] & nums[2]


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        
        nums.sort()
        
        if nums[-1] > 0:
            if nums[-2]*nums[-3] > nums[0]*nums[1]:
                return nums[-1]*nums[-2]*nums[-3]  
            else: return nums[-1]*nums[0]*nums[1]
        else:
            return nums[0]*nums[1]*nums[2]
        
        