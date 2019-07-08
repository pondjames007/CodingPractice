class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        
        points.sort()
        
        ans = 1
        end = points[0][1]
        
        for l, r in points[1:]:
            if l > end:
                ans += 1
                end = r
            else:
                end = min(end, r)
                
        return ans
        