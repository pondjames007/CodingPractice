# TIPS:
# A Pure Math Problem
# take positive target as example (negative is totally the same with reversed sign)
# To find smallest k, we all use +
# 1 + 2 + 3 + ... + k = target + d, where 0 <= d < k
# 1. if d == 0: k is the answer
# 2. if d % 2 == 0: 1 + 2 + 3 + ... -i + ... + k = target, where i == d/2
# 3. if d % 2 == 1:
#       a. k % 2 == 0: 1 + 2 + 3 + ... -i + ... + k + (k+1) = target, where i == ((k+1) + d) / 2 <= k
#       b. k % 2 == 1: 1 + 2 + 3 + ... -i + ... + k - (k+1) + (k+2) = target, where i = ((k+2) - (k+1) + d) / 2 = (d+1)/2 <= k
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        sum_ = 0
        
        while sum_ < target: 
            k += 1
            sum_ += k
            
        d = sum_ - target
        if d % 2 == 0: return k
        return k + 1 + k % 2