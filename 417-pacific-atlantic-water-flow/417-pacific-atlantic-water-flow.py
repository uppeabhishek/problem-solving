class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m, n = len(heights), len(heights[0])
        
        pacific_queue, atlantic_queue = deque([]), deque([])
        pacific_set, atlantic_set = set(), set()
        
        for i in range(m):
            for j in range(n):
                
                current = (i, j)
                
                if i == m - 1 or j == n - 1:
                    atlantic_queue.append(current)
                    atlantic_set.add(current)
                    
                if i == 0 or j == 0:
                    pacific_queue.append(current)
                    pacific_set.add(current)
                
        
        paths = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        
        def isValid(x, y):
            return not (x < 0 or y < 0 or x == m or y == n)
            
        def helper(queue, current_set):
            
            visited = set()
            
            while len(queue):
                x, y = queue.popleft()
                
                for path in paths:
                    
                    x1, y1 = x + path[0], y + path[1]
                    
                    current = (x1, y1)
                    
                    if isValid(x1, y1) and heights[x1][y1] >= heights[x][y] and current not in visited:
                        current_set.add(current)
                        queue.append(current)
                        visited.add(current)
    

        helper(pacific_queue, pacific_set)
        helper(atlantic_queue, atlantic_set)
    
        return atlantic_set.intersection(pacific_set)
        
            
        