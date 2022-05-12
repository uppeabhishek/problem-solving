from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:

    def getGridValue(self, grid, r1, c1, r2, c2):
        val = -1
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                print(i, j)
                if val == -1:
                    val = grid[i][j]
                else:
                    if val != grid[i][j]:
                        return False, val

        return True, val

    def helper(self, grid, r1, c1, r2, c2):
        if r2 < 1:
            return

        is_same, val = self.getGridValue(grid, r1 - 1, c1 - 1, r2 - 1, c2 - 1)

        if is_same:
            return
        else:
            r2_mid, c2_mid = r2 // 2, c2 // 2
            self.helper(grid, r1, c1, r2_mid, c2_mid)
            self.helper(grid, r1, c2_mid + 1, r2_mid, c2)
            self.helper(grid, r2_mid + 1, c1, r2, c2_mid)
            self.helper(grid, r2_mid + 1, c2_mid + 1, r2, c2)

    def construct(self, grid: List[List[int]]) -> 'Node':
        self.helper(grid, 1, 1, len(grid), len(grid))


if __name__ == "__main__":
    s = Solution()
    s.construct([[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0],
                 [1, 1, 1, 1, 0, 0, 0, 0]])
