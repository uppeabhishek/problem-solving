class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def helper(i, j):  
                                             
            if j == len(p):
                res = i == len(s)
            else:       
                first = i < len(s) and (s[i] == p[j] or p[j] == '.')
                
                if j + 1 < len(p) and p[j + 1] == '*':
                    res = (helper(i, j + 2)) or (first and helper(i + 1, j))
                else:
                    res = first and helper(i + 1, j + 1)
                
            return res
        return helper(0, 0)
    
    
                
                