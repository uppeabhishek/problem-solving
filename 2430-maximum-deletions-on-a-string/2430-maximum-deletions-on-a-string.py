class Solution:
    def deleteString(self, s: str) -> int:
        
        n = len(s)
        
        if len(set(s)) == 1:
            return n
        
        @cache    
        def helper(index, increment):
            nonlocal n
            
            if index == n - 1:
                return 1    
            
            if increment > (n // 2):
                return 0
            
            first, second, third = 0, 0, 1
            
            second_index = index + increment
                        
            if s[index : second_index] == s[second_index: second_index + increment]:
                first = 1 + helper(second_index, 1)
                second = helper(index, increment + 1)
            else:
                second = helper(index, increment + 1)
                            
            return max(first, second, third)
            
                
        return helper(0, 1)            
                