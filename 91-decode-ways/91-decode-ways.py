class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == '0':
            return 0
        
        n = len(s)
        
        @cache
        def helper(index):
            
            count = 0
            
            if index == n:
                return 1
            
            if s[index] == '0':
                return 0
            
            first, second = 0, 0
            
            if index + 1 < n and int(s[index: index + 2]) <= 26:
                first += helper(index + 2)
            
            second += helper(index + 1)
                       
            return first + second
    
        return helper(0)
            
        
    
        