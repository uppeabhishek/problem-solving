class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        queue = deque([("0000", 0)])
        visited = set(["0000"])
        deadends = set(deadends)
        
        if "0000" in deadends:
            return -1

        
        while len(queue):
            
            top, distance = queue.popleft()
            
            if top == target:
                return distance
    
            next_paths = []
            
            for i, t in enumerate(top):                
                up_current = top[:i] + str((int(top[i]) + 1) % 10) + top[i+1:]
                
                if (int(top[i]) - 1) == -1:
                    down_current = top[:i] + "9" + top[i+1:]
                else:
                    down_current = top[:i] + str(int(top[i]) - 1) + top[i+1:]
                    
                if up_current not in visited and up_current not in deadends:
                    queue.append((up_current, distance + 1))
                    visited.add(up_current)
                
                if down_current not in visited and down_current not in deadends:
                    queue.append((down_current, distance + 1))
                    visited.add(down_current)
                                
        return -1
        