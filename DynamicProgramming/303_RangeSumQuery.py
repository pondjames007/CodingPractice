# TIPS:
# preprocess the sum first

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.mem = []
        
        if nums:
            self.mem.append(nums[0])
            for num in nums[1:]:
                self.mem.append(self.mem[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        if not self.mem: return 0    
        
        if i == 0:
            return self.mem[j]
        
        return self.mem[j] - self.mem[i-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)