class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)


        i, j = 0, n - 1 
        
        while i < n:
            
            i1, j1 = i, j
            
            low, high = i, j

            for _ in range(i1, n - 1):
                
                temp1, temp2, temp3, temp4 = matrix[low][i1], matrix[i1][high], matrix[high][j1], matrix[j1][low]
                
                matrix[i1][high] = temp1
                matrix[high][j1] = temp2
                matrix[j1][low] = temp3
                matrix[low][i1] = temp4
            
                i1, j1 = i1 + 1, j1 - 1
            
            n, i, j = n - 1, i + 1, j - 1