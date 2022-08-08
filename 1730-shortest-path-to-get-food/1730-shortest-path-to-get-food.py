class Solution:
    
    def isValid(self, i, j, rows, cols, grid):
        return not (i < 0 or j < 0 or i == rows or j == cols or grid[i][j] == "X")
    
    def getFoodHelper(self, grid, i, j, rows, cols):
        
        min_distance = sys.maxsize
        
        queue = deque([(i, j, 0)])
        
        paths = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        visited = set([(i, j)])
                
        cnt = 0
        
        while len(queue):
            
            i, j, distance = queue.popleft()
                    
            tup = (i, j)
            
            if grid[i][j] == "#":
                min_distance = distance
                break
                
            for path in paths:
                i1, j1 = i + path[0], j + path[1]
                if self.isValid(i1, j1, rows, cols, grid) and (i1, j1) not in visited:
                    queue.append((i1, j1, distance + 1))     
                
                visited.add((i1, j1))
            
            cnt += 1
        
        return -1 if min_distance == sys.maxsize else min_distance
    
    def getFood(self, grid: List[List[str]]) -> int:
        source = ()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "*":
                    source = (i, j)
                    break
                
        return self.getFoodHelper(grid, source[0], source[1], len(grid), len(grid[0]))
    