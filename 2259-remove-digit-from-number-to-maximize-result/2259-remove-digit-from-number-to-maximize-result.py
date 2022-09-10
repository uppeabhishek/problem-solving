class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_res = 0
        for i, n in enumerate(number):
            if n == digit and i + 1 < len(number) and number[i + 1] > digit:
                max_res = number[0:i] + number[i + 1:]
                break
        
        if not max_res:
            for i, n in enumerate(number):
                if n == digit:
                    last_index = i
            
            return number[0:last_index] + number[last_index + 1:]
        
        return max_res
                