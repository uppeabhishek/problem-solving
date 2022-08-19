class Solution:
    def numberOfWays(self, s: str) -> int:
        
        n = len(s)
        
        right_prefix_zeros, right_prefix_ones = [0] * len(s), [0] * len(s)
        
        result = 0
        
        def helper():
            
            nonlocal result
            
            for i in range(n - 1, -1, -1):
                if s[i] == '1':
                    right_prefix_ones[i] = right_prefix_ones[i + 1] + 1 if i + 1 < n else 1
                    right_prefix_zeros[i] = right_prefix_zeros[i + 1] if i + 1 < n else 0
                else:
                    right_prefix_zeros[i] = right_prefix_zeros[i + 1] + 1 if i + 1 < n else 1
                    right_prefix_ones[i] = right_prefix_ones[i + 1] if i + 1 < n else 0
            
            
            i = 0
            zeros = 0

            while i < n:
                if s[i] == '1':
                    ones = 0
                    while i < n and s[i] == '1':
                        i += 1
                        ones += 1
                    
                    if i != n:
                        result += ones * zeros * right_prefix_zeros[i]
                else:
                    zeros += 1
                    i += 1
            
            i = 0
            ones = 0

            while i < n:
                if s[i] == '0':
                    zeros = 0
                    while i < n and s[i] == '0':
                        i += 1
                        zeros += 1
                    
                    if i != n:
                        result += ones * zeros * right_prefix_ones[i]
                else:
                    ones += 1
                    i += 1
                    
        helper()

        return result
            
            
            
            