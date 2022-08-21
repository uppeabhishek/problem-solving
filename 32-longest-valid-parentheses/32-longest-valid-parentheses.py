class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = [-1]
        
        max_val = 0
        
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not len(stack):
                    stack.append(i)
                else:
                    max_val = max(max_val, i - stack[-1])
                    
        return max_val
                        
                    