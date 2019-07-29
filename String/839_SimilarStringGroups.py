# TIPS:
# BRUTE FORCE + Union Find
# TLE
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        n = len(A)
        dsu = UnionSet(n)
        
        for i in range(n):
            for j in range(i+1, n):
                if self.similar(A[i], A[j]):
                    dsu.merge(i, j)
                    
        return dsu.size
    
    def similar(self, x, y):
        diff = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                diff += 1
                if diff > 2: return False
        return True
            
            
        
class UnionSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = n
        
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
            
        return self.parents[x]
    
    def merge(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return
        if self.rank[py] > self.rank[px]:
            px, py = py, px
        elif self.rank[py] == self.rank[px]:
            self.rank[px] += 1
        self.parents[py] = px
        self.size -= 1

# SUPER FAST SOLUTION, UNION FIND
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        m, n = len(A[0]), len(A)
        A = set(A)
        p, res = {s : s for s in A}, len(A) # p: parent
        def find(s):
            while s != p[s]: 
                p[s] = p[p[s]]
                s = p[s]
            return s
        def judge(a, b):
            cnt = 0
            for i, j in zip(a, b):
                if i != j:
                    if cnt < 2: cnt += 1
                    else: return False
            return cnt == 2
        if m > n:
            for a, b in itertools.combinations(A, 2): # O(m * n ^ 2)
                if judge(a, b):
                    ra, rb = find(a), find(b)
                    if ra != rb: res, p[ra] = res - 1, rb
        else: 
            for a in A: # O(n * m ^ 2)
                for i, j in itertools.combinations(range(m), 2):
                    b = a[:i] + a[j] + a[i + 1: j] + a[i] + a[j + 1:]
                    if b in A: 
                        ra, rb = find(a), find(b)
                        if ra != rb: res, p[ra] = res - 1, rb
        return res
