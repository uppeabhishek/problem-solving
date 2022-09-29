class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        m, n = len(grid1), len(grid1[0])
        
        def valid(i, j):
            nonlocal m, n
            return not (i < 0 or j < 0 or i == m or j == n)
        
        
        def helper(x, y):
            
            if not valid(x, y):
                return True
                                
            if grid2[x][y] == 0:
                return True
                        
            if grid1[x][y] == 0:
                return False
            
            grid1[x][y], grid2[x][y] = 0, 0
                        
            first, second, third, fourth = helper(x - 1, y), helper(x, y - 1), helper(x + 1, y), helper(x, y + 1)
            
            return first & second & third & fourth
                    
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if helper(i, j):
                        count += 1
        
        return count     
        
        
            
            
            