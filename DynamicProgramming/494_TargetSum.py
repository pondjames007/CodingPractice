# TIPS:
# Bitwise (TLE)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        ans = 0
        for i in range(2**len(nums)):
            res = 0
            for j in range(len(nums)):
                if i & 1 << j: res += nums[len(nums)-j-1]
                else: res -= nums[len(nums)-j-1]
            
            if res == S: ans += 1
                
        return ans

# Pure Search (TLE)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        ans = [0]
        self.lookup(nums, S, 0, 0, ans)
        
        return ans[0]
    
    
    def lookup(self, nums, S, idx, sum_, ans):
        if idx == len(nums):
            if sum_ == S:
                ans[0] += 1
            return
        
        self.lookup(nums, S, idx+1, sum_+nums[idx], ans)
        self.lookup(nums, S, idx+1, sum_-nums[idx], ans)
        
        return

# Search w/ Memoization (20%)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        mem = {}
        self.lookup(nums, mem, S, len(nums))
        
        return mem[(S, len(nums))]
    
    
    def lookup(self, nums, mem, S, idx):
        if idx == 0:
            if S != 0:
                mem[(S, idx)] = 0
            else:
                mem[(S, idx)] = 1
            return
        
        
        if (S-nums[idx-1], idx-1) not in mem:
            self.lookup(nums, mem, S-nums[idx-1], idx-1)
        if (S+nums[idx-1], idx-1) not in mem:
            self.lookup(nums, mem, S+nums[idx-1], idx-1)
        
        
        mem[(S, idx)] = mem[(S-nums[idx-1], idx-1)] + mem[(S+nums[idx-1], idx-1)]
        return

# DP
# use dict instead of array since we only need some of the results in a range
class Solution:
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)