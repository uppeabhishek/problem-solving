class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        h1, m1 = list(map(int, current.split(":")))
        h2, m2 = list(map(int, correct.split(":")))
        
        result = 0
        diff = 0
        
        result += h2 - h1
        
        if m1 > m2: 
            result -= 1
            diff = m2 + (60 - m1)
        else:
            diff = m2 - m1
            
        if diff >= 15:
            rem = diff // 15
            diff = diff - (rem * 15)
            result += rem

        if diff >= 5:
            rem = diff // 5
            diff = diff - (rem * 5)
            result += rem
        
        result += diff
            
        return result
    
        