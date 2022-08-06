class Solution:
    
    
    def appendToQueue(self, s, wordDict, queue, start, visited):
        for c in wordDict:
            tup = (start, start + len(c))
            if s[start:].startswith(c) and tup not in visited:
                visited.add(tup)
                queue.append((start, start + len(c)))
        
    
    def wordBreakHelper(self, s, wordDict):
        
        queue = deque([])
        visited = set()
        
        self.appendToQueue(s, wordDict, queue, 0, visited)        
        
        while len(queue):   
                        
            start, end = queue.popleft()
            
            if end == len(s):
                return True
        
            self.appendToQueue(s, wordDict, queue, end, visited)
    
        return False
    
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.wordBreakHelper(s, wordDict)