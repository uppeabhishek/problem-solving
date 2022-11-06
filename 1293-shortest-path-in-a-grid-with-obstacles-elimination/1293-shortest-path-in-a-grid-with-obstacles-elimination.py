class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        queue = deque([(0, 0, 0, k)])
        seen = set([(0, 0, k)])
        
        m, n = len(grid), len(grid[0])
        
        paths = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        
        
        def valid(i, j):
            return not (i < 0 or j < 0 or i == m or j == n)
        
        while len(queue):
                        
            i, j, distance, current_k = queue.popleft()
                        
            if i == m - 1 and j == n - 1:
                return distance
            
            for i1, j1 in paths:
                i2, j2 = i1 + i, j1 + j
            
                if valid(i2, j2) and (i2, j2, current_k) not in seen:
                    if grid[i2][j2] == 1:
                        if current_k > 0:
                            queue.append((i2, j2, distance + 1, current_k - 1))
                            
                    else:
                        queue.append((i2, j2, distance + 1, current_k))
                    
                    seen.add((i2, j2, current_k))
        return -1
                        
                    
                    
                    
                    