class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        def bottom_dp():
            
            maxArea = 0

            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    matrix[i][j] = int(matrix[i][j])
                    if matrix[i][j] == 1:
                        maxArea = 1
            
            
            paths = [[-1, -1], [-1, 0], [0, -1]]
            
                        
            for i in range(m):
                for j in range(n):
                    if i == 0 or j == 0:
                        continue
                    elif matrix[i][j] != 0:
                        noZeros = True
                        minVal = sys.maxsize
                        for path in paths:
                            i1, j1 = i + path[0], j + path[1]
                            if matrix[i1][j1] == 0:
                                noZeros = False
                                break
                            else:
                                minVal = min(minVal, matrix[i1][j1])

                        if noZeros:
                            val = matrix[i][j] + minVal
                            maxArea = max(maxArea, val * val)
                            matrix[i][j] = val
            
            return maxArea
            
        return bottom_dp()