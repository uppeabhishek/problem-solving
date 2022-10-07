class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        forbidden = set(forbidden)
        queue = deque([(0, 0, False)])
        visited = set([0])
        limit = 2000 + 2 * b
        
        while len(queue):
            top, distance, isBackward = queue.popleft()
            
            if top == x:
                return distance
            
            left = top - b
            right = top + a
            
            if left > -1 and left not in visited and left not in forbidden and not isBackward: 
                queue.append((left, distance + 1, True))
                visited.add(left)  
            
            if right < limit and right not in forbidden and right not in visited:
                queue.append((right, distance + 1, False))
                visited.add(right)
                
        return -1
            
            
            