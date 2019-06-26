# TIPS:
# * DFS
# * go through whole board find out the first one and do dfs to all 4 directions

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def find(board, i, j , word):
            if len(word) == 0: return True
            if i<0 or i>len(board)-1 or j<0 or j>len(board[i])-1 or word[0] != board[i][j]: 
                return False
            
            tmp = board[i][j]
            board[i][j] = '#'
            res = find(board, i+1, j, word[1:]) or find(board, i-1, j, word[1:]) or find(board, i, j+1, word[1:]) or find(board, i, j-1, word[1:])
            board[i][j] = tmp
            return res
            
        
        if not board: return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if find(board, i, j, word): return True
                
        return False