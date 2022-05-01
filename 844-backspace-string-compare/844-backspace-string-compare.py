class Solution:
    
    def helper(self, s):
        stack = []
        for c in s:
            if c == "#":
                if len(stack):
                    stack.pop()
            else:
                stack.append(c)
        return stack
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = self.helper(s)
        s2 = self.helper(t)
        return s1 == s2