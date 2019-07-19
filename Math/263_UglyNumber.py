# TIPS:
# keep dividing the number with 2, 3, 5
# if at the end it is 1 -> true
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0: return False
        if num == 1: return True
        
        prime = [2,3,5]
        
        for p in prime:
            while num % p == 0:
                num /= p
                
        if num != 1: return False
        
        return True