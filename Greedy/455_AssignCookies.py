# TIPS:
# * can also use bisect (slower)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s: return 0
        
        g.sort()
        s.sort()
        ans = 0
        while len(g) > 0 and len(s) > 0:
            if g[-1] > s[-1]:
                g.pop()
            else:
                ans += 1
                g.pop()
                s.pop()
        return ans