class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
    
        stack = []
        for i in num + '0':
            while k > 0 and len(stack) > 0 and i < stack[-1]:
                stack.pop()
                k -= 1
            if len(stack) + int(i):
                stack.append(i)

        if len(stack):
            stack.pop()
        return ''.join(stack) if len(stack) else '0'