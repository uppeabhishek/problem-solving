from copy import copy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        result = []

        def recursion(index):

            if index == len(nums):
                result.append(copy(nums))
                return

            for i in range(index, len(nums)):
                swap(i, index)
                recursion(index + 1)
                swap(i, index)

        recursion(0)


s = Solution()
s.permute([1, 2, 3])
