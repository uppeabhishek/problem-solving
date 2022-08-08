class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = s.count("1")
        zeros = 0
        
        result = ones
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                ones -= 1
            else:
                zeros += 1
                        
            result = min(result, ones + zeros)
    
        return result