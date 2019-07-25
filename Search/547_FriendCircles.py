# TIPS:
# * DFS recursion
# * Almost the same way as #200
# * you don't need to use 'seen' to store whether it is used or not
#   you can use M[i][i] and change it to 0 or whatever to label it is used (not suggested)
# * enumerate all student, then use DFS to go through all his friend, then kick them out

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
                
# Union-Find Set
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        s = UnionFindSet(n)
        
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1: s.Union(i, j)
        
        circles = set()
        for i in range(n):
            circles.add(s.Find(i))
            
        return len(circles)
        
        
class UnionFindSet:
    def __init__(self, n):
        self.parents = [0]*(n+1) # every node is independent, don't care 0, node i has id i
        self.ranks = [0]*(n+1)
        
        for i in range(n+1):
            self.parents[i] = i

    def Find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.Find(self.parents[x])
        
        return self.parents[x]

    def Union(self, x, y):
        px, py = self.Find(x), self.Find(y)
        if px == py: return False # they are in the same cluster
        
        if self.ranks[px] > self.ranks[py]: self.parents[py] = px
        if self.ranks[py] > self.ranks[px]: self.parents[px] = py
        if self.ranks[px] == self.ranks[py]:
            self.parents[py] = px
            self.ranks[px] += 1

        return True