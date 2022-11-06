from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        c = Counter(nums)

        def dp(index):

            if index < 0:
                return 0

            first = dp(index - 1)

            current = nums[index]
            value = 0

            i, j, k = 0, 0, 0

            if c[current]:
                i = c[current]
                c[current] -= 1
                value = current

            if c[current - 1]:
                j = c[current - 1]
                c[current - 1] = 0

            if c[current + 1]:
                k = c[current + 1]
                c[current + 1] = 0

            second = value + dp(index - 1)

            c[current], c[current - 1], c[current + 1] = i, j, k

            return max(first, second)

        return dp(len(nums) - 1)