# TIPS:
# Use Binary Search in the distance and find the total pairs in that distance
# When the pair > k -> the value is low

import bisect

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        low = 0
        high = nums[-1] - nums[0]
        
        while low < high:
            mid = (low + high)//2
            
            if self.find_pairs(nums, mid) < k:
                low = mid + 1
            else:
                high = mid
        
        return low
                        
    def find_pairs(self, nums, dist):
        ans = 0
        
        for i in range(len(nums)):
            # with the base (i), add the dist to it and find the index
            # the index means the value before it has distance (between i) < dist
            ans += bisect.bisect(nums, nums[i] + dist, lo = i) - i - 1
        return ans
                
                    