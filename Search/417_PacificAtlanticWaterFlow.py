# TIPS:
#
# Brute Force: TLE O(4^mn)
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.lookup(matrix, i, j, matrix[i][j]) == 3:
                    ans.append([i,j])
                    
        return ans
    
    
    def lookup(self, matrix, x, y, h):
        # '1' == reach P, '2' == reach A, '0' == cannot reach any
        # OR every lookups of 4 directions, if the result is '3' -> it can reach both P and A
        # (1 | 2 == 3)
        
        if x < 0 or y < 0: return 1
        if x == len(matrix) or y == len(matrix[0]): return 2
        if matrix[x][y] > h: return 0 # if the current node is higher than the previous node
        
        h = matrix[x][y]
        matrix[x][y] = float('inf')
        
        valid = self.lookup(matrix, x-1, y, h) | \
                self.lookup(matrix, x+1, y, h) | \
                self.lookup(matrix, x, y-1, h) | \
                self.lookup(matrix, x, y+1, h)
                
        matrix[x][y] = h
        
        return valid


# Reverse the operation, check how far can a point on the border can go
# Those points can flow to P/A
# Check if the point can flow to both P and A
# O(mn + (m+n))
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        
        n = len(matrix)
        m = len(matrix[0])
        
        P = [[False]*m for _ in range(n)]
        A = [[False]*m for _ in range(n)]
        
        for x in range(m):
            self.lookup(matrix, x, 0, 0, P)
            self.lookup(matrix, x, n-1, 0, A)
        
        for y in range(n):
            self.lookup(matrix, 0, y, 0, P)
            self.lookup(matrix, m-1, y, 0, A)
            
        ans = []
        for i in range(n):
            for j in range(m):
                if P[i][j] and A[i][j]: ans.append([i,j])
        
        return ans
    
    def lookup(self, matrix, x, y, h, points):
        if x < 0 or y < 0 or x == len(matrix[0]) or y == len(matrix): return
        
        if points[y][x] or matrix[y][x] < h: return
        
        points[y][x] = True
        
        self.lookup(matrix, x+1, y, matrix[y][x], points)
        self.lookup(matrix, x-1, y, matrix[y][x], points)
        self.lookup(matrix, x, y-1, matrix[y][x], points)
        self.lookup(matrix, x, y+1, matrix[y][x], points)
        self.lookup(matrix, x+1, y, matrix[y][x], points)
        

# DP -> use BFS
# for every node, ask neighbor nodes if they can reach P/A
# dp[i][j] := reachable to P/A (0 = cannot, 1 = can reach P, 2 = can reach A, 1+2 = can reach both)
# dp[i][j] |= dp[y][x] if there is an edge in G
# When to stop? if there is no more changes
# this method has risk, since you don't know when it will stop (may be really slow)
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        
        n = len(matrix)
        m = len(matrix[0])
        
        dp = [[0]*m for _ in range(n)]
        
        for x in range(m):
            dp[0][x] |= 1
            dp[n-1][x] |= 2
        
        for y in range(n):
            dp[y][0] |= 1
            dp[y][m-1] |= 2
            
        dirs = [0, -1, 0, 1, 0]
        
        while True:
            changed = False
            for y in range(n):
                for x in range(m):
                    for d in range(4):
                        tx = x + dirs[d]
                        ty = y + dirs[d+1]
                        
                        if tx < 0 or ty < 0 or tx == m or ty == n \
                            or matrix[y][x] < matrix[ty][tx] or \
                            (dp[y][x] | dp[ty][tx]) == dp[y][x]: 
                            continue
                        dp[y][x] |= dp[ty][tx]
                        changed = True
                        
            if not changed: break
        
        ans = []
        for i in range(n):
            for j in range(m):
                if dp[i][j] == 3: ans.append([i, j])
                    
        return ans
                    