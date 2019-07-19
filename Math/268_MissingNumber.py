# TIPS:
# sum up n numbers and subtract sum(nums) can find out the missing number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n_sum = sum(range(len(nums)+1))
        m_sum = sum(nums)
        
        return n_sum - m_sum
        