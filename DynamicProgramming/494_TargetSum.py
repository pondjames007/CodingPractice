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
# dp[i][j] := sum j using first i elements
# dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j+nums[i-1]]
# dp[0][0] = 1 -> Special Case
# since it is sparse, you can use hash table to store the value
class Solution:
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        
        n = len(nums)
        s_range = sum(nums)
        dp = [[0]*(2*s_range+1) for _ in range(n+1)]
        dp[0][0] = 1


        for i in range(1, n+1):
            for j in range(-s_range,s_range+1):
                dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j+nums[i-1]]
                
        return dp[n][S] if S <= s_range and S >= -s_range else 0

# DP
# use dict instead of array since we only need some of the results in a range
class Solution:
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            dp = {}
            for d in dic:
                dp[d + nums[i]] = dp.get(d + nums[i], 0) + dic.get(d, 0)
                dp[d - nums[i]] = dp.get(d - nums[i], 0) + dic.get(d, 0)
            dic = dp
        return dic.get(S, 0)


        