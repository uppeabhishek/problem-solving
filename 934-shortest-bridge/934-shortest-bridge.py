class Solution:
    
    def __init__(self):
        self.paths = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        
    def valid(self, grid, i, j):
        return not (i < 0 or j < 0 or i == len(grid) or j == len(grid))
    
    def DFS(self, grid, i, j, visited, queue, original_color, new_color):
        
        queue.append((i, j, -1))
        grid[i][j] = new_color
        
        
        for i1, j1 in self.paths:
            i2, j2 = i + i1, j + j1
            
            if self.valid(grid, i2, j2) and (i2, j2) not in visited and grid[i2][j2] == original_color:
                self.DFS(grid, i2, j2, visited, queue, original_color, new_color)
            
            visited.add((i2, j2))    
            
        
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        queue = deque([])
        
        
        for i in range(n):
            color = False
            for j in range(n):
                if grid[i][j] == 1:
                    self.DFS(grid, i, j, set([(i, j)]), queue, 1, 2)
                    color = True
                    break
            
            if color:
                break
        
        visited = set([(queue[0][0], queue[0][1])])
        
        while len(queue):
            
            i, j, distance = queue.popleft()
            
            if grid[i][j] == 1:
                return distance
            
            for i1, j1 in self.paths:
                
                i2, j2 = i + i1, j + j1
                
                if self.valid(grid, i2, j2) and (i2, j2) not in visited:
                    queue.append((i2, j2, distance + 1))
                
                visited.add((i2, j2))

            
        