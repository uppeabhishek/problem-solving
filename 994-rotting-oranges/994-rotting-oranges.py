class Solution:
    
    def isValid(self, i, j, rows, cols, grid):
        return not (i < 0 or j < 0 or i == rows or j == cols or grid[i][j] == 0)
        
    def orangesRottingHelper(self, grid, source, rows, cols):
        queue = deque([])
        
        for s in source:
            queue.append((s[0], s[1], 0))
        
        paths = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        max_time = 0
        
        while len(queue):
            i, j, time = queue.popleft()
            
            max_time = max(max_time, time)
            
            for path in paths:
                i1, j1 = path[0] + i, path[1] + j
                if self.isValid(i1, j1, len(grid), len(grid[0]), grid) and grid[i1][j1] == 1:
                    grid[i1][j1] = 2
                    queue.append((i1, j1, time + 1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return max_time
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        source = set([])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    source.add((i, j))
                
        return self.orangesRottingHelper(grid, source, len(grid), len(grid[0]))