class Solution:
    
    def appendToQueue(self, s, wordDict, queue, start, prev):
        for i, c in enumerate(wordDict):
            tup = (start, start + len(c))
            if s[start:].startswith(c):
                queue.append((prev + str(i), start, start + len(c)))
        
    
    def wordBreakHelper(self, s, wordDict):
        
        queue = deque([])
        result = []
        
        self.appendToQueue(s, wordDict, queue, 0, '')        
        
        while len(queue):   
                        
            index, start, end = queue.popleft()
            
            if end == len(s):
                temp = []
                for i in index:
                    temp.append(wordDict[int(i)])
                
                result.append(" ".join(temp))
                
            
            self.appendToQueue(s, wordDict, queue, end, str(index))
    
        
        return result
    
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.wordBreakHelper(s, wordDict)