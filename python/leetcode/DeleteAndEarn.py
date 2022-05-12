from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        min_val = min(nums)
        numbers = [0] * (max(nums) - min_val + 1)

        if len(numbers) == 1:
            return sum(nums)

        for num in nums:
            numbers[num - min_val] += num

        dp = [0] * len(numbers)
        dp[0] = numbers[0]
        dp[1] = max(numbers[0], numbers[1])

        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i - 2] + numbers[i])

        return dp[-1]


s = Solution()
s.deleteAndEarn(
    [10, 8, 4, 2, 1, 3, 4, 8, 2, 9, 10, 4, 8, 5, 9, 1, 5, 1, 6, 8, 1, 1, 6, 7, 8, 9, 1, 7, 6, 8, 4, 5, 4, 1, 5, 9, 8, 6,
     10, 6, 4, 3, 8, 4, 10, 8, 8, 10, 6, 4, 4, 4, 9, 6, 9, 10, 7, 1, 5, 3, 4, 4, 8, 1, 1, 2, 1, 4, 1, 1, 4, 9, 4, 7, 1,
     5, 1, 10, 3, 5, 10, 3, 10, 2, 1, 10, 4, 1, 1, 4, 1, 2, 10, 9, 7, 10, 1, 2, 7, 5])
