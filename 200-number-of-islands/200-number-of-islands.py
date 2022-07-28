class Solution:
    
    def isValid(self, i, j, rows, cols):
        return not (i < 0 or j < 0 or i == rows or j == cols)
        
    def numIslandsHelper(self, grid, i, j, visited):
        current = (i, j)
        if not (self.isValid(i, j, len(grid), len(grid[0])) and current not in visited and grid[i][j] == '1'):
            return
        
        visited.add(current)
        grid[i][j] = '-1'
        
        self.numIslandsHelper(grid, i - 1, j, visited)
        self.numIslandsHelper(grid, i, j - 1, visited)
        self.numIslandsHelper(grid, i + 1, j, visited)
        self.numIslandsHelper(grid, i, j + 1, visited)
            
    
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited:
                    if grid[i][j] == '1':
                        cnt += 1
                        self.numIslandsHelper(grid, i, j, visited)
        return cnt
                