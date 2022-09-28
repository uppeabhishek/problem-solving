class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        def valid(i, j):
            nonlocal m, n
            return not (i < 0 or j < 0 or i == m or j == n)
        
                
        def helper(i, j):
            
            if not valid(i, j):
                return False
            
            if grid[i][j] == 1:
                return True
            
            grid[i][j] = 1
                        
            first, second, third, fourth = helper(i - 1, j), helper(i, j - 1), helper(i + 1, j), helper(i, j + 1)
            
            return first & second & third & fourth
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if helper(i, j):
                        count += 1                    
        
        return count
            