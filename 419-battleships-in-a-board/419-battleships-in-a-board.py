class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        def valid(i, j):
            return not (i < 0 or j < 0 or i == len(board) or j == len(board[0])) and board[i][j] != '.'
        
        def helper(i, j):
            
            if board[i][j] == '.':
                return 
            
            board[i][j] = '.'
            
            paths = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            
            for path in paths:
                i1, j1 = path[0] + i, path[1] + j
                if valid(i1, j1):
                    helper(i1, j1)
            
        
        result = 0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    helper(i, j)
                    result += 1
        
        return result
            