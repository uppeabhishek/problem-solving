class Solution:
    def numSplits(self, s: str) -> int:
        
        c1, c2 = defaultdict(int), defaultdict(int)
        
        for c in s:
            c2[c] += 1
        
        result = 0
        
        for c in s:
            c2[c] -= 1
            c1[c] += 1
            
            if c2[c] == 0:
                del c2[c]
            
            
            if len(c1) == len(c2):
                result += 1
        
        return result
        