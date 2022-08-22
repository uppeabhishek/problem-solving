class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        dic = defaultdict(int)
        left = 0
        result = 0
        max_val = 0
        
        for right in range(len(s)):
            
            dic[s[right]] = 1 + dic[s[right]]
            
            max_val = max(max_val, dic[s[right]])
                    
            while right - left + 1 - max_val > k:
                dic[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result