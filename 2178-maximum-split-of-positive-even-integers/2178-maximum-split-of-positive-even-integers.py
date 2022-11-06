class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        
        if finalSum & 1 == 1:
            return []
        
        result = []
        current = 2
        
        while finalSum:
            if finalSum - current <= current:
                result.append(finalSum)
                break
            result.append(current)
            finalSum -= current
            current += 2
        
        return result
        
