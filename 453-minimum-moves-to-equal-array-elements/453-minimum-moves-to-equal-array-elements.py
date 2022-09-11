class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        result = 0
        for i in range(len(nums) - 1):
            result += (i + 1) * (nums[i] - nums[i + 1])
        return result
    