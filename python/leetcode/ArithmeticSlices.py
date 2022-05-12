from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        k, cnt, result = 2, 2, 0
        prev, current = nums[0] - nums[1], nums[1] - nums[k]

        while k < len(nums):
            if prev == current:
                cnt += 1
            else:
                result += (cnt - 2) * (cnt - 1) // 2
                cnt = 2
            prev = current

            if k + 1 == len(nums):
                result += (cnt - 2) * (cnt - 1) // 2
                break

            current = nums[k] - nums[k + 1]
            k += 1

        return result


s = Solution()
s.numberOfArithmeticSlices([1, 2, 3, 4])
s.numberOfArithmeticSlices([1, 3, 5, 6, 7, 8])
s.numberOfArithmeticSlices([3, 4, 23, 12, 23, 11, 23, 12, 13, 14, 16, 8, 10, 2, 4, 6, 8])
