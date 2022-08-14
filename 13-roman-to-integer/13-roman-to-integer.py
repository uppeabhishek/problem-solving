class Solution:
    def romanToInt(self, s: str) -> int:
        
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
                
        result = 0
        
        i = 0
        
        while i < len(s):
            
            c = s[i]
            
            if i + 1 < len(s):
                if dic[s[i + 1]] > dic[s[i]]:
                    result += dic[s[i + 1]] - dic[s[i]]
                    i += 2
                else:
                    result += dic[c]
                    i += 1
            else:
                result += dic[c]
                i += 1
        
        return result