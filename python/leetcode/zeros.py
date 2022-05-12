from typing import List


class Solution:
    def count_trailing_zeros(self, num):
        cnt = 0
        while num:
            rem = num % 10
            if rem == 0:
                cnt += 1
            else:
                break
            num = num // 10

        return cnt

    def is_valid(self, i, j, rows, cols):
        if i < 0 or j < 0 or i == rows or j == cols:
            return False
        return True

    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        result = []
        rows, cols = [], []
        for i, g in enumerate(grid):
            current = []
            for j, c in enumerate(g):
                if c % 10 == 0:
                    first = self.count_trailing_zeros(c)
                    second = 0
                    if self.is_valid(i - 1, j, len(grid), len(grid[0])):
                        second = max(second, self.count_trailing_zeros(c * grid[i - 1][j]))

                    if self.is_valid(i, j - 1, len(grid), len(grid[0])):
                        second = max(second, self.count_trailing_zeros(c * grid[i][j - 1]))

                    if self.is_valid(i, j + 1, len(grid), len(grid[0])):
                        second = max(second, self.count_trailing_zeros(c * grid[i][j + 1]))

                    if self.is_valid(i + 1, j, len(grid), len(grid[0])):
                        second = max(second, self.count_trailing_zeros(c * grid[i + 1][j]))
                    current.append(max(first, second))
                else:
                    current.append(0)

            rows.append(max(current))
            result.append(current)

        # for i, g in enumerate(result):
        #     max_till_now = 0
        #     for j, c in enumerate(g):
        #         pass
        #         # print(i, j)
        #         # if result[j][i] > max_till_now:
        #         #     max_till_now = c
        #     cols.append(max_till_now)

        result = 0

        for i in range(0, len(rows) - 1):
            result = max(result, rows[i] + rows[i + 1])

        for i in range(0, len(cols) - 1):
            result = max(result, cols[i] + cols[i + 1])

        return result


s = Solution()
s.maxTrailingZeros([[10], [10], [10000]])
