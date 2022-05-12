class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                current = 0
                while len(stack):
                    if stack[-1] == "(":
                        stack.pop()
                        break
                    else:
                        current += stack[-1]
                        stack.pop()
                if not current:
                    stack.append(1)
                else:
                    stack.append(2 * current)

        return sum(stack)


s = Solution()
# s.scoreOfParentheses("()")
# s.scoreOfParentheses("(())")
# s.scoreOfParentheses("()()")
# s.scoreOfParentheses("(()(()))")
s.scoreOfParentheses("()()((()))()()(())()()()(())((((()))))")
