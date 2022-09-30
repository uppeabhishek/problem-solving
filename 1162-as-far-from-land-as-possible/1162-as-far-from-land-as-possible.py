class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        
        n = len(grid)
        paths = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def valid(i, j):
            return not (i < 0 or j < 0 or i == n or j == n)
        
        def BFS(current_set):
            
            queue = deque([])
            visited = set()
            
            flag = False
            
            for i, j in current_set:
                
                if not flag:
                    visited.add((i, j))
                    
                queue.append((i, j, 0))
                flag = True
                                    
            while len(queue):
                
                i, j, distance = queue.popleft()
                                                
                for i1, j1 in paths:
                    i2, j2 = i + i1, j + j1
                    if valid(i2, j2) and (i2, j2) not in visited and (i2, j2) not in current_set:
                        grid[i2][j2] = min(grid[i2][j2], distance + 1)
                        queue.append((i2, j2, distance + 1))
                    
                    visited.add((i2, j2))
                    
        one, zero = False, False
        
        current_set = set()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    zero = True
                    grid[i][j] = sys.maxsize
                else:
                    one = True
                    current_set.add((i, j))
        
        if not (one and zero):
            return -1
        
        BFS(current_set)
        
        max_val = 1
        
        for i in range(n):
            for j in range(n):
                max_val = max(max_val, grid[i][j])
            
        return max_val