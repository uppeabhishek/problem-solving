class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        i, j = 0, 0
        cnt = 0
        
        while True:
                
            prev_j = j
            
            while i < len(source) and j < len(target):
                if source[i] == target[j]:
                    j += 1
                i += 1
            
            cnt += 1
            
            if j == len(target):
                return cnt
            
            if i == len(source):
                if prev_j == j:
                    return -1
                i = 0
        