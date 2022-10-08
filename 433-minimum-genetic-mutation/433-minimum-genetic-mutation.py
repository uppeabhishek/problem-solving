class Solution:
    
    def getNextMutations(self, string, bank):
        result = []
        
        for b in bank:
            count = 0
            for i in range(len(string)):
                if string[i] != b[i]:
                    count += 1
                
                if count > 1:
                    break
            
            if count == 1:
                result.append(b)
        
        return result
        
        
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        queue = deque([(start, 0)])
        
        visited = set([start])
        
        while len(queue):
            top, distance = queue.popleft()
            
            if top == end:
                return distance
            
            mutations = self.getNextMutations(top, bank)
            
            for mutation in mutations:
                if mutation not in visited:
                    queue.append((mutation, distance + 1))
                    visited.add(mutation)
            
        return -1
            
        
        
        