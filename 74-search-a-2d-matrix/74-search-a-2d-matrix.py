class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])

        def getIndex(index):
            return index // cols, index % cols
        
        def bsearch(low, high):
            
            if low > high:
                return False
            
            mid = low + (high - low) // 2
            
            i, j = getIndex(mid)
                        
            if matrix[i][j] == target:
                return True
            
            elif target < matrix[i][j]:
                return bsearch(low, mid - 1)
            
            return bsearch(mid + 1, high)
                
        return bsearch(0, rows * cols - 1)
            
        
        