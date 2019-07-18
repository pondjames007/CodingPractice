# TIPS:
# make a map of sum and frequency
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        ans = 0
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            sub = sum_ - k
            
            if sub in dic:
                ans += dic[sub]
            
            if sum_ not in dic:
                dic[sum_] = 1
            else:
                dic[sum_] += 1
        return ans           
            
        