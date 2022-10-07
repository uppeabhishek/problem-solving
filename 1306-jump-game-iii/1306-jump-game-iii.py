class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        n = len(arr)
        visited = set([start])
        queue = deque([start])
        
        while len(queue):
            
            top = queue.popleft()
            
            if arr[top] == 0:
                return True
            
            left_index = top - arr[top]
            right_index = top + arr[top]
            
            if left_index > -1 and left_index not in visited:
                queue.append(left_index)
                visited.add(left_index)
            
            if right_index < n and right_index not in visited:
                queue.append(right_index)   
                visited.add(right_index)
        
        return False