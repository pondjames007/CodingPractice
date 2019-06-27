# TIPS:
# * use STACK
# * go through whole grid and find out '1'

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        island_num = 0
        
        stack = []
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    stack.append([i,j])
                    
                    while stack:
                        [r,c] = stack.pop()
                        grid[r][c] = '2'
                        
                        if r > 0 and grid[r-1][c] == '1': stack.append([r-1, c])
                        if r < len(grid)-1 and grid[r+1][c] == '1': stack.append([r+1,c])
                        if c > 0 and grid[r][c-1] == '1': stack.append([r, c-1])
                        if c < len(grid[r])-1 and grid[r][c+1] == '1': stack.append([r, c+1])
            
                    island_num += 1
        
        return island_num
    
            