class Solution:
    def numDecodings(self, s: str) -> int:

        def isValid(c):
            if c[0] == '0':
                return False
            c = int(c)

            return 1 <= c <= 26

        def dp(i, j):

            if i == len(s):
                return 1
            elif j == len(s):
                return 0

            first, second = 0, 0

            if isValid(s[i]):
                first = dp(i + 1, j + 1)

            if i + 1 < len(s) and isValid(s[i: i + 2]):
                second = dp(i + 2, j + 2)

            return first + second

        return dp(0, 0)


s = Solution()
s.numDecodings("226")
s.numDecodings("06")
