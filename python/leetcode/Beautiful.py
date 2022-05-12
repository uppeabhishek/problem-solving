from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        max_len = len(nums)
        i = 0
        index = 0
        cnt = 0
        while i < max_len - 1:
            if index % 2 == 0 and nums[i] == nums[i + 1]:
                i += 1
                cnt += 1
            else:
                i += 1
                index += 1

        if len(nums) - cnt & 1 == 1:
            return cnt + 1

        return cnt


s = Solution()
# s.minDeletion([1, 1, 2, 2, 3, 3])
# s.minDeletion([1, 1, 2, 2, 3, 3])
s.minDeletion([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3])
