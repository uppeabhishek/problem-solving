class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        
        paths = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]
        
        
        def BFS():
            queue = deque([(0, 0, 0)])
                
            visited = set([(0, 0)])
            
            while len(queue):
                x1, y1, distance = queue.popleft()
                
                if x1 == x and y1 == y:
                    return distance
            
                for path in paths:
                    
                    x2, y2 = x1 + path[0], y1 + path[1]
                    
                    current = (x2, y2)
                    
                    if current not in visited:
                        queue.append((x2, y2, distance + 1))
                        visited.add(current)
                    
        return BFS()
                
                