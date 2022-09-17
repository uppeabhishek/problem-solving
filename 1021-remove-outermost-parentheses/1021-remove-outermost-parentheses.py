class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        stack = []
        primitive = []
        result = []
        
        
        for i, c in enumerate(s):
            if c == '(':
                if not len(stack):
                    primitive.append(i)
                else:
                    result.append(c)
                stack.append(i)
            else:
                top = stack[-1]
                
                if s[top] == '(':
                    if top == primitive[-1]:
                        primitive.append(i)
                    else:
                        result.append(c)
                    stack.pop()
                else:
                    stack.append(i)
                    result.append(c)
        
        return "".join(result)
        
        