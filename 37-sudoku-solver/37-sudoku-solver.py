class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        n = len(board)
        rowSize = n // 3
        
        rowSets, colSets, boxSets = [set() for _ in range(n)], [set() for _ in range(n)], [set() for _ in
                                                                                               range(n)]
        def getBoxIndex(i, j):
            return ((i // rowSize) * rowSize) + (j // rowSize)
        
        def helper(i, j):
                                 
            if i == n - 1 and j == n:
                return True
            elif j == n:
                i = i + 1
                j = 0
            
            current_val = board[i][j]
            
            if current_val != '.':
                return helper(i, j + 1)
            
            for k in range(1, n + 1):
                
                val = str(k)
                
                if val in rowSets[i] or val in colSets[j] or val in boxSets[getBoxIndex(i, j)]:
                    continue
            
                board[i][j] = val
                rowSets[i].add(val)
                colSets[j].add(val)
                boxSets[getBoxIndex(i, j)].add(val)

                if helper(i, j + 1):
                    return True

                board[i][j] = '.'
                rowSets[i].remove(val)
                colSets[j].remove(val)
                boxSets[getBoxIndex(i, j)].remove(val)
            
            return False
            
        for i in range(n):
            for j in range(n):
                current_val = board[i][j]
                
                if board[i][j] != ".":
                    rowSets[i].add(current_val)
                    colSets[j].add(current_val)
                    boxSets[getBoxIndex(i, j)].add(current_val)
                    
        helper(0, 0)
                    