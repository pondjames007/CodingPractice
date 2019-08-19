# TIPS:
# 
# It can be treated as a Multi-source, Multi-destination shortest path problem
# DFS + BFS
# Use DFS to find first island, and turn them to 2 (#200)
# Use BFS to expand one island until it reaches the second one
import queue

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        # DFS
        q = queue.Queue()
        found = False
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    self.dfs(A, j, i, q)
                    found = True
                    break
            if found: break
        
        # BFS
        steps = 0
        dirs = [0, 1, 0, -1, 0]
        while not q.empty():
            size = q.qsize()
            while size:
                size -= 1
                x, y = q.get()
                for i in range(4):
                    # use 1d array to describe 2d 4 directions
                    tx = x + dirs[i]
                    ty = y + dirs[i+1]
                    if tx < 0 or ty < 0 or tx >= len(A[0]) or ty >= len(A) or A[ty][tx] == 2: continue
                    if A[ty][tx] == 1: return steps
                    A[ty][tx] = 2
                    q.put((tx, ty))
            steps += 1
        
        return -1
        
    def dfs(self, A, x, y, q):
        if x < 0 or y < 0 or x >= len(A[0]) or y >= len(A) or A[y][x] != 1: return
        
        A[y][x] = 2
        q.put((x, y))
        self.dfs(A, x-1, y, q)
        self.dfs(A, x+1, y, q)
        self.dfs(A, x, y-1, q)
        self.dfs(A, x, y+1, q)
        
                    
