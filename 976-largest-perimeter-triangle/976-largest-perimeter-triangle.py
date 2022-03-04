class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(0, len(nums) - 2):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                res = max(res, nums[i] + nums[i + 1] + nums[i + 2])
        return res