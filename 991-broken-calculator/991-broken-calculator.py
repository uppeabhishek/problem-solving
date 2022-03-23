class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue > target:
            return startValue - target
        
        result = 0
        while startValue != target:
            if target & 1 == 0 and target > startValue:
                target //= 2
            else:
                target += 1
            result += 1
        return result