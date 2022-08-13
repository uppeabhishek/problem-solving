class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        n = len(s)
        
        max_len, max_val = 0, None
        
        for i in range(n):
            
            # even
            
            a, b = i, i
            
            while a > -1 and b < n:
                if s[a] != s[b]:
                    break
                
                if b - a + 1 > max_len:
                    max_val = s[a: b + 1]
                    max_len = b - a + 1
                
                a -= 1
                b += 1
            
            # odd
            
            a, b = i, i + 1
            while a > -1 and b < n:
                if s[a] != s[b]:
                    break
                
                if b - a + 1 > max_len:
                    max_val = s[a: b + 1]
                    max_len = b - a + 1
                
                a -= 1
                b += 1
        
        return max_val
        