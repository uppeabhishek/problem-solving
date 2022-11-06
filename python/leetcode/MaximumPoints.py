class Solution:
    def maxPoints(self, points) -> int:

        def helper(row, col):
            current = 0

            if row == len(points):
                return current

            for i in range(len(points[row])):
                current = max(current, points[row][i] + helper(row + 1, i))

            return current

        print(helper(0, 0))


s = Solution()
s.maxPoints([[1, 2, 3], [1, 5, 1], [3, 1, 1]])
