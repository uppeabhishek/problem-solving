class Solution:
    
    def cleanString(self, s):
        current = []
        
        i = 0
        
        while i < len(s):
            if s[i] != '{':
                current.append([s[i]])
                i += 1
            else:
                i += 1
                temp = []
                
                while s[i] != '}':
                    if s[i] != ',':
                        temp.append(s[i])        
                    i += 1
                current.append(temp)
                i += 1
        
        return current
    
    def helper(self, i, j, s, current, result):
                
        if i == len(s):
            result.append("".join(current))
            return
    
        
        for j in range(len(s[i])):
            current.append(s[i][j])
            self.helper(i + 1, j, s, current, result)
            current.pop()
        
    def expand(self, s: str) -> List[str]:
        
        cleanedString = self.cleanString(s)
        
        result = []
                
        self.helper(0, 0, cleanedString, [], result)
        
        result.sort()
        
        return result
        
        
        
        