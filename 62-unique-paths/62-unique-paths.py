class Solution:
    
    def isValid(self, i, j, rows, cols):
        return not (i < 0 or j < 0 or i == rows or j == cols)
    
    def uniquePathsHelper(self, matrix, i, j, rows, cols, dic):
        
        key = (i, j)
        
        if key in dic:
            return dic[key]
        
        res = 0
        if i == rows - 1 and j == cols - 1:
            return 1
        
        paths = [[0, 1], [1, 0]]
        
        for path in paths:
            i1, j1 = i + path[0], j + path[1]
            if self.isValid(i1, j1, rows, cols):
                res += self.uniquePathsHelper(matrix, i1, j1, rows, cols, dic)
        
        dic[key] = res
        return dic[key]

    def uniquePaths(self, m: int, n: int) -> int:
        
        dic = {}
        
        matrix = [[0 for _ in range(m)] for _ in range(n)]

        return self.uniquePathsHelper(matrix, 0, 0, m, n, dic)
    