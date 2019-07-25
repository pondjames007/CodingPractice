# TIPS:
# binary search with some variations

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l = 1
        r = max(piles) + 1
        
        while l < r:
            m = (l+r)//2
            
            time = 0
            for p in piles:
                time += p//m
                if p%m != 0: time += 1
                
            if time > H:
                l = m+1
            else:
                r = m
        
        return l