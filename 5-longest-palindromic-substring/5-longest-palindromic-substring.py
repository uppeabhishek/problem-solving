class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # odd length    
        max_odd_len = 0
        i = 0
        max_odd_len_str = s[0]
        while i < len(s):
            cur_len = 0
            
            prev, nxt = i - 1, i + 1
            
            while prev > -1 and nxt < len(s) and s[prev] == s[nxt]:
                prev -= 1
                nxt += 1
                cur_len += 2
            
            
            if cur_len > max_odd_len:
                max_odd_len_str = s[prev + 1:nxt]
                max_odd_len = cur_len
            
            i += 1        
    
    
        # even length
        max_even_len = 0
        i = 0
        max_even_len_str = s[0]
        while i < len(s):
            cur_len = 0
            
            prev, nxt = i - 1, i
            
            while prev > -1 and nxt < len(s) and s[prev] == s[nxt]:
                prev -= 1
                nxt += 1
                cur_len += 2
            
            if cur_len > max_even_len:
                max_even_len_str = s[prev + 1:nxt]
                max_even_len = cur_len
            
            i += 1        

        if max_even_len > max_odd_len:
            return max_even_len_str
        
        return max_odd_len_str
