class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        result = 0
        
        while target != 1 and maxDoubles:
            if target & 1 == 1:
                target -= 1
            else:
                target //= 2
                maxDoubles -= 1
            
            result += 1
        
        result += target - 1
        
        return result