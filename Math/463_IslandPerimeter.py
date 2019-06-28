# TIPS:
# * go through whole grid and store every island edge by checking neihbor

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        
        edges = []
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    edge = 4
                    
                    if i > 0 and grid[i-1][j] == 1:
                        edge -= 1
                    if i < len(grid)-1 and grid[i+1][j] == 1:
                        edge -= 1
                    if j > 0 and grid[i][j-1] == 1:
                        edge -= 1
                    if j < len(grid[i])-1 and grid[i][j+1] == 1:
                        edge -= 1
                    edges.append(edge)
        return sum(edges)