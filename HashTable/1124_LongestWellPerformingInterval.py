# TIPS:
#
# Running Sum (Prefix Sum)
# TLE
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        sum_ = [0]*(n+1)
        for i in range(1, n+1):
            sum_[i] = sum_[i-1] + (1 if hours[i-1] > 8 else -1)
            
        ans = 0
        for i in range(n+1):
            for j in range(i+1, n+1):
                if sum_[j] - sum_[i] > 0:
                    ans = max(ans, j-i)
                    
        return ans

# Target Sum
# hours[i] > 8 -> 1, hours[i] <= 8 -> -1
# To make the longest interval, the sum should be 1
# The question is reduced to find out the longest interval for target sum
# ALSO: if sum(v[0:n]) > 0 return n
# 
# Use a hashtable to store the **first** index of the cumulative sum
# ans = max(ans, i - index[sum-1]) (Because s - (s-1) = 1) 
# 當前的0~i的和為s 要找到某個idx他的0~idx的和是s-1, 如此index相減就會是和為1的interval
# T: O(n)
# S: O(n)
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        idx = {}
        ans = 0
        s = 0
        
        for i in range(len(hours)):
            s += 1 if hours[i] > 8 else -1
            
            if s > 0: # sum(0~i) is valid, and should be longest
                ans = i + 1
            else:
                if s not in idx: idx[s] = i
                if s-1 in idx: # find out the first idx that appears s-1 
                    ans = max(ans, i-idx[s-1])
                    
        return ans