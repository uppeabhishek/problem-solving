class Solution:
    
    def addToResult(self, result, value, length):
        if not len(result):
            result.append([value, length])
        else:
            if result[-1][0] == value:
                result[-1][1] += length
            else:
                result.append([value, length])
        
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        
        i, j = 0, 0
        
        m, n = len(encoded1), len(encoded2)
        
        result = []
        
        while i < m and j < n:
            
            a, b = encoded1[i]
            
            c, d = encoded2[j]
            
            if b == d:
                self.addToResult(result, a * c, b)
                i += 1
                j += 1
            elif b < d:
                self.addToResult(result, a * c, b)
                encoded2[j][1] = d - b
                i += 1
            else:
                self.addToResult(result, a * c, d)
                encoded1[i][1] = b - d
                j += 1
        
        return result
            
            
            
            