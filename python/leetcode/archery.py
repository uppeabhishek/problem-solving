from copy import copy
from typing import List


class Solution:

    def __init__(self):
        self.cache = {}
        self.max_val = -1
        self.max_result = []
        self.current_result = [0] * 12

    def helper(self, points, numArrows, aliceArrows, index):
        key = (points, numArrows)

        if key in self.cache:
            return self.cache[key]

        if numArrows == 0 or index < 0:
            if numArrows == 0:
                if points > self.max_val:
                    self.max_val = points
                    self.max_result = copy(self.current_result)
            return points

        if numArrows > aliceArrows[index]:
            # pick the arrow
            prev = self.current_result[index]
            self.current_result[index] = (numArrows - aliceArrows[index]) if index == 0 else aliceArrows[index] + 1
            pick = self.helper(points + index, numArrows - aliceArrows[index] - 1, aliceArrows, index - 1)
            self.current_result[index] = prev

            # dont pick the arrow
            dont_pick = self.helper(points, numArrows, aliceArrows, index - 1)

            self.cache[key] = max(pick, dont_pick)
            return self.cache[key]

        self.cache[key] = self.helper(points, numArrows, aliceArrows, index - 1)
        return self.cache[key]

    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        self.helper(0, numArrows, aliceArrows, 11)


s = Solution()
# s.maximumBobPoints(9, [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0])
# s.maximumBobPoints(100000, [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2])
s.maximumBobPoints(8, [0, 1, 0, 2, 0, 0, 1, 0, 1, 0, 1, 2])
