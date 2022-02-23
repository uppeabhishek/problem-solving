class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        set_le = len(set(s))
        dic = {}
        i, j = len(s) - 1, set_le
        while j > 0:
            if s[i] not in dic:
                dic[s[i]] = i
                j -= 1
            i -= 1

        stack = []
        visited = [False] * 26
        for i in range(len(s)):
            c = s[i]
            ord_c = ord(c) - 97
            if len(stack) == 0:
                stack.append(c)
                visited[ord_c] = True
            elif c > stack[-1]:
                if not visited[ord_c]:
                    stack.append(c)
                    visited[ord_c] = True
            elif not visited[ord_c]:
                while len(stack):
                    if c <= stack[-1] and dic[stack[-1]] > i:
                        visited[ord(stack[-1]) - 97] = False
                        stack.pop()
                    else:
                        break
                stack.append(c)
                visited[ord_c] = True

        return "".join(stack)


if __name__ == "__main__":
    s = Solution()
    # s.removeDuplicateLetters("cbacdcbc")
    # s.removeDuplicateLetters("bcabc")
    # s.removeDuplicateLetters("cdadabcc")
    s.removeDuplicateLetters("abacb")
