# TIPS:
#
# 1st Approach: Union Find Faces:
# Divide each grid into 4 triangles, and merge those triangles accordingly.
# Ans = # of roots in DSU
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        
        dsu = UnionSet(4*n*n)
        for row in range(n):
            for col in range(n):
                idx = 4*(row*n + col)
                if grid[row][col] == '/':
                    dsu.union(idx+0, idx+3)
                    dsu.union(idx+1, idx+2)
                elif grid[row][col] == '\\':
                    dsu.union(idx+0, idx+1)
                    dsu.union(idx+2, idx+3)
                elif grid[row][col] == ' ':
                    dsu.union(idx+0, idx+1)
                    dsu.union(idx+1, idx+2)
                    dsu.union(idx+2, idx+3)
                
                if row+1 < n:
                    dsu.union(idx+2, idx+4*n+0)
                if col+1 < n:
                    dsu.union(idx+1, idx+4+3)
                    
        ans = 0
        for i in range(4*n*n):
            if dsu.find(i) == i: ans += 1

        return ans
                    
                        
        
class UnionSet:
    def __init__(self, n):
        self.parents = [0]*n
        
        for i in range(n):
            self.parents[i] = i
            
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]
    
    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)


# Approach 2: Euler Formula
# V - E + F = C + 1 (Vertices + Edges + Faces = ConnectedComponents + 1)
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dsu = UnionSet(n)
        # All vertices on the boundaries are merged into root(0)
        for r in range(n+1):
            for c in range(n+1):
                if r == 0 or r == n or c == 0 or c == n:
                    dsu.p[dsu.getIndex(n, r, c)] = 0
                else:
                    dsu.p[dsu.getIndex(n, r, c)] = dsu.getIndex(n, r, c)
                    
        f = 1
        for r in range(n):
            for c in range(n):
                if grid[r][c] == ' ': continue
                # A new face will be created if 2 vertices are in the same group
                if grid[r][c] == '/':
                    f += dsu.merge(dsu.getIndex(n, r, c+1), dsu.getIndex(n, r+1, c))
                else:
                    f += dsu.merge(dsu.getIndex(n, r, c), dsu.getIndex(n, r+1, c+1))
                    
                    
        return f
        
        
class UnionSet:
    def __init__(self, n):
        self.p = [0]*((n+1)*(n+1))
        
    def getIndex(self, n, r, c):
        return r*(n+1)+c
    
    def find(self, x):
        if(self.p[x] != x): self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def merge(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry: return 1
        self.p[ry] = self.p[rx]
        
        return 0
        

# Approach 3: Pixelation (Upscale 3 times)
# Use DFS to find connect components
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        g = [[0]*(n*3) for _ in range(n*3)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    g[i*3 + 0][j*3 + 2] = 1
                    g[i*3 + 1][j*3 + 1] = 1
                    g[i*3 + 2][j*3 + 0] = 1
                elif grid[i][j] == '\\':
                    g[i*3 + 0][j*3 + 0] = 1
                    g[i*3 + 1][j*3 + 1] = 1
                    g[i*3 + 2][j*3 + 2] = 1
        
        ans = 0
        for i in range(3*n):
            for j in range(3*n):
                if g[i][j]: continue
                self.visit(g, i, j, 3*n)
                ans += 1
                
        return ans
    
    
    def visit(self, g, x, y, n):
        if x < 0 or x >= n or y < 0 or y >= n: return
        if g[x][y]: return
        g[x][y] = 1
        self.visit(g, x+1, y, n)
        self.visit(g, x, y+1, n)
        self.visit(g, x-1, y, n)
        self.visit(g, x, y-1, n)
        