# TIPS:
# * Use HASH TABLE (DICTIONARY) will be faster than only list

class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        if not nums: return []
        
        table = {val: idx for idx, val in enumerate(nums)}
        
        for i, v in enumerate(nums):
            sub = target - v
            if sub in table and i != table[sub]:
                return [i, table[sub]]