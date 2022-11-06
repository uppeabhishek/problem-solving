from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        def dp(start, end):
            if start == len(multipliers) or end == len(nums) - len(multipliers):
                return 0

            first = nums[start] * multipliers[start] + dp(start + 1, end - 1)
            second = nums[end] * multipliers[start] + dp(start + 1, end - 1)

            return max(first, second)

        print(dp(0, len(nums) - 1))


s = Solution()
# s.maximumScore([1, 2, 3], [3, 2, 1])
s.maximumScore([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6])
