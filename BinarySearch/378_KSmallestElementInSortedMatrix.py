# TIPS:
# use value to be the searching basis
# count how many numbers are larger than m
# use bisect to each row can count

import bisect
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = matrix[0][0]
        r = matrix[-1][-1]
        
        while l < r:
            m = (l+r)//2
            t = 0
            for row in matrix:
                t += bisect.bisect(row, m)
                
            if t >= k:
                r = m
            else:
                l = m+1
                
        return l