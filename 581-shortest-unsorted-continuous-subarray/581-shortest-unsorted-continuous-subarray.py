class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums1 = sorted(nums)
        left_i, right_i = -1, -2
        for i in range(len(nums)):
            if nums[i] != nums1[i]:
                if left_i == -1:
                    left_i = i
                else:
                    right_i = i
        return right_i - left_i + 1