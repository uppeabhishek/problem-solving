class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def helper(i, j):
                        
            if i == len(s):
                if j == len(p):
                    return True
                
                if p[j] == '*':
                    return helper(i, j + 1)
                else:
                    return False
                
            
            if j == len(p):
                return i == len(s)
            
            if (i < len(s) and s[i] == p[j]) or p[j] == '?':
                return helper(i + 1, j + 1)

            elif j < len(p) and p[j] == '*':
                return helper(i, j + 1) or helper(i + 1, j + 1) or helper(i + 1, j)
            
            return False
        
        return helper(0, 0)