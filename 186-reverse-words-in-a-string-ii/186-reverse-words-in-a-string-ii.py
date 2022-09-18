class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def reverse(i, j):        
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            
        reverse(0, len(s) - 1)
        
        i, j = 0, 0
        
        while j < len(s):
            
            while j < len(s) and s[j] != " ":
                j += 1
            
            reverse(i, j - 1)
            
            i, j = j + 1, j + 1
            
            
            
            
            