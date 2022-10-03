class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        m, n = len(maze), len(maze[0])
        ei, ej = entrance
        
        queue = deque([])
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    if maze[i][j] == '.' and not (i == ei and j == ej):
                        queue.append((i, j, 0))
                
        if not len(queue):
            return -1
        
        
        def valid(i, j):
            return not (i < 0 or j < 0 or i == m or j == n)
            
        
        visited = set([(queue[0][0], queue[0][1])])
        
        distance = 0
        
        paths = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        while len(queue):
            i, j, distance = queue.popleft()
            
            if i == ei and j == ej:
                return distance
            
            for i1, j1 in paths:
                i2, j2 = i + i1, j + j1
                
                if valid(i2, j2) and (i2, j2) not in visited and maze[i2][j2] == '.':
                    queue.append((i2, j2, distance + 1))
                
                visited.add((i2, j2))
                    
        return -1
    
            
            