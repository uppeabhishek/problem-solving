import sys
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dp(i, prev):

            if i == len(nums):
                return 0

            first, second = 0, 0

            if nums[i] > prev:
                first = 1 + dp(i + 1, nums[i])

            second = dp(i + 1, prev)

            return max(first, second)

        return dp(0, -sys.maxsize)


s = Solution()
s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
s.lengthOfLIS([0, 1, 0, 3, 2, 3])
s.lengthOfLIS([10, 22, 9, 33, 21, 50, 41, 60, 80])
