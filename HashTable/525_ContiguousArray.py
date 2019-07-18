# TIPS:
# change 0 to -1, calculate the sum
# if the sum is already in count, current idx - previous idx of that sum will be a potential answer
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = {} # <sum_, idx>
        ans = 0
        sum_ = 0
        
        for i in range(len(nums)):
            if nums[i] == 0: sum_ -= 1
            else: sum_ += 1
            
            if sum_ == 0: ans = i+1
            else:
                if sum_ in count: 
                    ans = max(ans, i - count[sum_])
                else:
                    count[sum_] = i
                
        return ans