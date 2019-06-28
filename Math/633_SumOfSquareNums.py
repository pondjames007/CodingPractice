# TIPS:
# * import math

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        bound = math.floor(math.sqrt(c))
        
        square = set(x*x for x in range(bound+1))
        
        for s in square:
            if c - s in square:
                return True
        
        return False