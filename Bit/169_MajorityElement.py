# TIPS:

# Use collections.Counter.most_common(n) to return the n-most common KEY and VALUE
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        return count.most_common(1)[0][0]

# Sort the list and return the element at middle
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

# Randomly pick the element and look if it is the majority
# Theoretically it is more than 50% to pick the majority
import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        while True:
            index = random.randrange(l)
            majority = nums[index]
            count = 0
            for ele in nums:
                if ele == majority: count += 1
                if count > l/2: return ele


# Use Boyer-Moore Voting Concept
# Since the majority is n/2+1, its count will remain 1 after subtracting all counts that are not equal to majority
# if count == 0 -> it is not the majority
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 0
        
        for num in nums:
            if num == majority: count += 1
            else:
                count -= 1
                if count == 0:
                    count = 1
                    majority = num
        return majority

# Bit Vote (it seems that Python is not good at handling bit manipulation in negative number)
# C++ version is good
# Since maj count > n/2: every bit should be dominated by the majority (if i-th bit of maj == 1, then we can count 1 in i-th bit of every number is > n/2)
# We treat the number as 32-bits (int)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        majority = 0
        for i in range(32):
            mask = 1 << i # i-th bit is 1, others 0
            count = 0
            for num in nums:
                if num & mask: count += 1 # count how many 1 appears on i-th bit
            
            if count > l/2: # i-th bit is 1
                majority |= mask # put 1 to majooritty's i-th bit 
        return majority