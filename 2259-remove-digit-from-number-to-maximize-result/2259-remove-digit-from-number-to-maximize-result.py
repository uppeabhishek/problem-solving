class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_res = 0
        for i, n in enumerate(number):
            if n == digit:
                max_res = max(max_res, int(number[0:i] + number[i + 1:]))
        
        return str(max_res)
                