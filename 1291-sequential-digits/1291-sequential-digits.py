class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        def getStartValue(digits):
            current = 0
            for i in range(1, digits):
                current += (10 ** (digits - i)) * i
            current += digits  
            
            return current
    
        def getIncrementValue(digits):
            current = 0
            for i in range(1, digits):
                current += 10 ** (digits - i)
            current += 1
            
            return current
        
        def getDigits(num):
            
            cnt = 0
            
            while num:
                num = num // 10
                cnt += 1
            
            return cnt
    
        
        i, j = getDigits(low), getDigits(high)

        result = []
        
        while i <= min(j, 9):            
            current = getStartValue(i)
            increment = getIncrementValue(i)
                        
            for _ in range(i, 10):  
                if current >= low and current <= high:
                    result.append(current)
                
                current += increment
            i += 1
            
        return result
        