class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        i, j, current = 0, 0, s[0]
        
        while i < len(s) and j < len(t):
            if current == t[j]:
                i+=1
                if i == len(s):
                    break
                current = s[i]
             
            j+=1
    
        return i == len(s)