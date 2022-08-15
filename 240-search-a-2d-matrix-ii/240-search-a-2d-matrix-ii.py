class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        
        
        def valid(i, j):
            return not (i < 0 or j < 0 or i == m or j == n)
        
        def helper():
            
            start = (0, n - 1)

            end = (m - 1, 0)

            while True:
                i, j = start
                
                if not valid(i, j):
                    return False
                                
                if matrix[i][j] == target:
                    return True
                elif target < matrix[i][j]:
                    start = (i, j - 1)
                else:
                    start = (i + 1, j)

            return False
        
        
        return helper()