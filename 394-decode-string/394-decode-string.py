class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                stack.append(num)
            elif s[i] == ']':
                char = deque()
                while len(stack):
                    if isinstance(stack[-1], int):
                        stack.append("".join(list(map(str, char)) * stack.pop()))
                        break
                    else:
                        char.appendleft(stack[-1])
                        stack.pop()
            else:
                stack.append(s[i])
            i += 1
        
        return "".join(stack)