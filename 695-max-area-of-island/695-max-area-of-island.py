class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
                
        m, n = len(grid), len(grid[0])
        
        def valid(i, j):
            nonlocal m, n
            return not (i < 0 or j < 0 or i == m or j == n)
        
            
        visited = set()
        result = 0
        paths = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        

        def helper(i, j):
            
            visited.add((i, j))
            grid[i][j] = 0
            self.cnt += 1
            
            for i1, j1 in paths:
                i2, j2 = i + i1, j + j1
                        
                if valid(i2, j2) and grid[i2][j2] == 1 and (i2, j2) not in visited:
                    helper(i2, j2)
                    
                    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.cnt = 0
                    helper(i, j)
                    result = max(result, self.cnt)
        
        return result