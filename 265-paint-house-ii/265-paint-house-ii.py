import sys
from functools import cache
from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:

        @cache
        def helper(i, prev_i):

            result = sys.maxsize

            if i == len(costs):
                return 0

            for index, cost in enumerate(costs[i]):
                if index != prev_i:
                    result = min(result, cost + helper(i + 1, index))

            return result

        return helper(0, -1)
