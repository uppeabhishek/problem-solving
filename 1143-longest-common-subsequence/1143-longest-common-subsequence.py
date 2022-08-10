class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
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
        
        return dp(0, 0)
        