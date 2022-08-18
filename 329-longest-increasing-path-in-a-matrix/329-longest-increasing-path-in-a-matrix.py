class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        paths = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        max_cnt = 1

        def valid(i, j):
            return not (i < 0 or j < 0 or i == m or j == n or matrix[i][j] == "#")

        @cache
        def helper(i, j):

            result = 1
            
            for path in paths:
                i1, j1 = path[0] + i, path[1] + j

                if valid(i1, j1):
                    if matrix[i1][j1] > matrix[i][j]:
                        result = max(result, 1 + helper(i1, j1))
            
            return result

        max_cnt = 1
        
        for i in range(m):
            for j in range(n):
                max_cnt = max(max_cnt, (helper(i, j)))
        
        return max_cnt