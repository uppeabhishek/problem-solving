class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        se = set()
        for i, c in enumerate(s):
            if c == "(":
                stack.append((c, i))
                se.add(i)
            elif c == ")":
                if len(stack) > 0:
                    if stack[-1][0] == "(":
                        se.remove(stack[-1][1])
                        stack.pop()
                    else:
                        stack.append((c, i))
                        se.add(i)
                else:
                    stack.append((c, i))
                    se.add(i)
        res = []
                
        for i, c in enumerate(s):
            if c != ")" and c != "(":
                res.append(c)
            else:
                if i not in se:
                    res.append(c)
            
        return "".join(res)
        