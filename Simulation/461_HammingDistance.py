# TIPS:
#
# Use Bit operation to calculate
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        
        for i in range(32):
            if x & 1 << i != y & 1 << i: ans += 1
                
        return ans

# Use XOR and calculate '1's (Faster)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        xor = x^y
        for _ in range(32):
            ans += xor & 1
            xor >>= 1
        
        return ans