# TIPS:
# Recursive Solution
# super slow
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        
        c = [0]*n
        l = [0]*n
        
        # Find the length LIS
        max_len = 0
        for i in range(n):
            max_len = max(max_len, self.check_len(l, nums, i))
        
        # Check all endings
        ans = 0
        for i in range(n):
            if self.check_len(l, nums, i) == max_len:
                ans += self.count(l, c, nums, i)
                
        return ans
    
    # Length of LIS ends with nums[n]
    def check_len(self, l, nums, n):
        if n == 0: return 1
        if l[n] > 0: return l[n]
        
        max_len = 1
        
        # check every subarray
        for i in range(n):
            if nums[n] > nums[i]:
                max_len = max(max_len, self.check_len(l, nums, i) + 1)
                
        l[n] = max_len
        return l[n]
    
    # Number of LIS ends with nums[n]
    def count(self, l, c, nums, n):
        if n == 0: return 1
        if c[n] > 0: return c[n]
        
        total_count = 0
        length = self.check_len(l, nums, n)
        for i in range(n):
            if nums[n] > nums[i] and self.check_len(l, nums, i) == length-1:
                total_count += self.count(l, c, nums, i)
                
        if total_count == 0:
            total_count = 1
            
        c[n] = total_count
        return c[n]

# DP
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        
        c = [1]*n
        l = [1]*n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if l[j] + 1 > l[i]:
                        l[i] = l[j] + 1
                        c[i] = c[j]
                    elif l[j] + 1 == l[i]:
                        c[i] += c[j]
                        
        max_len = max(l)
        ans = 0
        for i in range(n):
            if l[i] == max_len:
                ans += c[i]
                
        return ans