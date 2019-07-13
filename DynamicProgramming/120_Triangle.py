# TIPS:
# TOP-DOWN save the result at every cell

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        t = triangle
        
        for i in range(n):
            for j in range(i+1):
                if i == 0 and j == 0: continue
                if j == 0: t[i][j] += t[i-1][j]
                elif j == i: t[i][j] += t[i-1][j-1]
                else: t[i][j] += min(t[i-1][j], t[i-1][j-1])
                    
        return min(t[n-1])