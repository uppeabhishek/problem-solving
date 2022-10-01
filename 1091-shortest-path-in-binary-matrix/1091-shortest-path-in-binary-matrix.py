class Solution:
    
    def valid(self, i, j, n):
        return not (i < 0 or j < 0 or i == n or j == n)
        
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        queue = deque([(0, 0, 1)])
        
        paths = [[-1, 0], [0, -1], [0, 1], [1, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]]
        
        visited = set([0, 0])
        
        while len(queue):
            
            i, j, distance = queue.popleft()
            
            if i == n - 1 and j == n - 1:
                return distance
            
            for i1, j1 in paths:
                
                i2, j2 = i + i1, j + j1
                
                if self.valid(i2, j2, n) and grid[i2][j2] == 0 and (i2, j2) not in visited:
                    queue.append((i2, j2, distance + 1))
                
                visited.add((i2, j2))
        
        return -1
                
        
        
        
                