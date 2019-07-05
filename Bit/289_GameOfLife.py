# TIPS:
# change 0 -> 2 if dead -> live and 1 -> 3 if live to dead

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                nb = self.check_nb(board, i, j)
                if board[i][j] == 0 and nb == 3:
                    board[i][j] = 2 # dead -> live
                elif board[i][j] == 1 and nb != 2 and nb != 3:
                    board[i][j] = 3 # live -> dead
                    
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 2: board[i][j] = 1
                elif board[i][j] == 3: board[i][j] = 0
        
        
        
    def check_nb(self, board, i, j):
        m,n = len(board), len(board[i])
        count = 0
        if i-1 >= 0 and j-1 >= 0:   count += board[i-1][j-1]%2
        if i-1 >= 0:                count += board[i-1][j]%2
        if i-1 >= 0 and j+1 < n:    count += board[i-1][j+1]%2
        if j-1 >= 0:                count += board[i][j-1]%2
        if j+1 < n:                 count += board[i][j+1]%2
        if i+1 < m and j-1 >= 0:    count += board[i+1][j-1]%2
        if i+1 < m:                 count += board[i+1][j]%2
        if i+1 < m and j+1 < n:     count += board[i+1][j+1]%2
        return count