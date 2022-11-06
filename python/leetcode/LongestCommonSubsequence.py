class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def dp(i, j):

            if i == len(text1) or j == len(text2):
                return 0

            first, second = 0, 0

            if text1[i] == text2[j]:
                first = 1 + dp(i + 1, j + 1)
            else:
                first = dp(i + 1, j)
                second = dp(i, j + 1)

            return max(first, second)

        m, n = len(text1), len(text2)

        def bottom_dp():

            matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]


            for i in range(m + 1):
                for j in range(n + 1):
                    if i == 0 or j == 0:
                        matrix[i][j] = 0
                    elif text1[i - 1] == text2[j - 1]:
                        matrix[i][j] = 1 + matrix[i - 1][j - 1]
                    else:
                        matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

        bottom_dp()


s = Solution()
s.longestCommonSubsequence("abcde", "ace")
s.longestCommonSubsequence("abc", "abc")
s.longestCommonSubsequence("abc", "def")
s.longestCommonSubsequence("AGGTAB", "GXTXAYB")
