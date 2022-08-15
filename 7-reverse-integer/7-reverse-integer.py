class Solution:
    def reverse(self, x: int) -> int:
        result = 0

        negative = False
        
        if x < 0:
            negative = True
            x = x * -1
            
        negative_max_val = (2 ** 31) / 10
        positive_max_val = (2 ** 31 - 1) / 10
        
        while x != 0:
            rem = x % 10
            result = result * 10 + rem
            
            if negative:
                if result / 10 > negative_max_val:
                    return 0
            else:
                if result / 10 > positive_max_val:
                    return 0
                
            x = x // 10
        
        if negative:
            result = result * -1
            
        return result