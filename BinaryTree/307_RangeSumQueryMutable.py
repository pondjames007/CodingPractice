# TIPS:
# Use Fenwick Tree (Bit Indexed Tree)
class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = FenwickTree(len(nums))
        self.nums = nums
        
        for i in range(len(nums)):
            self.tree.update(i+1, nums[i])

    def update(self, i: int, val: int) -> None:
        self.tree.update(i+1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.tree.query(j+1) - self.tree.query(i)
        
class FenwickTree:
    def __init__(self, n):
        self.sums_ = [0] * (n+1)
        
    def lowbit(self, x): return x & (-x)
    
    def update(self, i, delta):
        while i < len(self.sums_):
            self.sums_[i] += delta
            i += self.lowbit(i)
            
    def query(self, i):
        sum_ = 0
        while i > 0:
            sum_ += self.sums_[i]
            i -= self.lowbit(i)
        
        return sum_