# TIPS:
# * DFS recursion

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def lookup(i, M):
            for j in range(len(M[i])):
                if M[i][j] == 1 and j not in seen:
                    seen.add(j)
                    lookup(j, M)
            return
        
        if not M: return 0
        
        seen = set()
        ans = 0
        for i in range(len(M)):
            if i not in seen:
                lookup(i, M)
                ans += 1
                
        return ans
                