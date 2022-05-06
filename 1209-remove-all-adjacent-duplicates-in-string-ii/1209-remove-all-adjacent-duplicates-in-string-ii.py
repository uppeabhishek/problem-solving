class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque([])
        
        cnt = 0
                
        for c in s:
            if len(stack) > 0:
                if stack[-1][0] == c:
                    stack[-1] = (c, stack[-1][1] + 1)
                else:
                    stack.append((c, 1))
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append((c, 1))
                
        return "".join([c[0] * c[1] for c in stack])