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