class Solution:
    def totalNQueens(self, n: int) -> int:
        
        queen = 'Q'
        empty = '.'
        
        matrix = [['.' for _ in range(n)] for _ in range(n)]
        
        def valid(i, j):
            for k in range(n):
                if matrix[k][j] == queen:
                    return False
            
            i1, j1 = i, j
            
            while j1 > -1:
                if matrix[i1][j1] == queen:
                    return False
                i1 -= 1
                j1 -= 1
            
            i1, j1 = i, j
            
            while j1 < n:
                if matrix[i1][j1] == queen:
                    return False
                i1 -= 1
                j1 += 1
                
            return True
        
        def helper(row):
                   
            res = 0
            
            if row == n:
                return 1
            
            for i in range(n):
                if valid(row, i):
                    matrix[row][i] = queen
                    res += helper(row + 1)
                matrix[row][i] = empty
            
            return res
            
        return helper(0)
                           
    
        