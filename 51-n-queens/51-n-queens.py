from copy import deepcopy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
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
        
        def helper(row, result):
                        
            if row == n:
                current = []
                for i in range(n):
                    temp = ""
                    for j in range(n):
                        temp += matrix[i][j]
                    current.append(temp)
                
                result.append(current)
                return 
            
            for i in range(n):
                if valid(row, i):
                    matrix[row][i] = queen
                    helper(row + 1, result)
                matrix[row][i] = empty
            
        result = []
        helper(0, result)
                
        return result
                    
    
        