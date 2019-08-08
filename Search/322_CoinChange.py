# TIPS:
# USE DP
# dp[i] := min num of coins to have value i
# dp[i] = min(dp[i-x] for x in coins)
# slower than greedy
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        
        # dp[i] := min num of coins to have value i
        dp = [-1]*(amount+1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            nums = [dp[i-x] for x in coins if i-x >= 0 and dp[i-x] >= 0]
            if nums:
                dp[i] = min(nums)+1
            
        return dp[-1]


# USE DFS
# greedy: only go through every coins from large to small
# count from largest possible number to 0
# always track the best one
# pass in reference only in mutable objects! immutable objects are not
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return -1
        
        coins.sort(reverse=True)
        
        ans = [float('inf')]
        self.lookup(coins, amount, 0, 0, ans)
        
        return int(ans[0]) if ans[0] != float('inf') else -1
    
    
    def lookup(self, coins, amount, idx, count, ans):
        coin = coins[idx]
        
        if idx == len(coins)-1:
            if amount%coin == 0:
                ans[0] = min(ans[0], count + amount/coin)
        else:
            k = amount//coin
            for i in range(k, -1, -1):
                if count + k >= ans[0]: continue
                
                self.lookup(coins, amount-i*coin, idx+1, count+i, ans)
        

        