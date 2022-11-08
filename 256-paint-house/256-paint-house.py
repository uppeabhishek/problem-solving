import sys
from functools import cache
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        @cache
        def helper(i, prev_i):

            result = sys.maxsize

            if i == len(costs):
                return 0

            for j in range(3):
                if j != prev_i:
                    result = min(result, costs[i][j] + helper(i + 1, j))

            return result

        return helper(0, -1)

