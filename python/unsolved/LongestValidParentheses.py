from collections import defaultdict


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        dic = defaultdict(int)
        max_till_now = 0

        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if len(stack) != 0:
                    if stack[-1] == "(":
                        stack.pop()
                        if dic[len(stack)] == 0:
                            dic[len(stack)] = 2
                            max_till_now = max(max_till_now, 2)
                        else:
                            dic[len(stack)] += 2
                            max_till_now = max(max_till_now, dic[len(stack)])
                    else:
                        stack.append(")")
                else:
                    stack.append(")")

        return max_till_now


if __name__ == "__main__":
    s = Solution()
    s.longestValidParentheses(")()())")
    s.longestValidParentheses("(()")
    s.longestValidParentheses("")
    s.longestValidParentheses("(()(()(()))(")
