from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        paths = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def valid(i, j):
            return not (i < 0 or j < 0 or i == m or j == n)

        dp = [[1 for _ in range(n)] for _ in range(m)]

        def helper():
            for i in range(m):
                for j in range(n):
                    for path in paths:
                        i1, j1 = i + path[0], j + path[1]
                        if valid(i1, j1):
                            if matrix[i1][j1] > matrix[i][j]:
                                dp[i1][j1] = dp[i][j] + 1

        helper()
        print(dp)


s = Solution()
s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
# s.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]])
# s.longestIncreasingPath([[7, 8, 9], [9, 7, 6], [7, 2, 3]])
