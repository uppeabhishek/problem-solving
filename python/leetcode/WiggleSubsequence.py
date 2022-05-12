from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        same = True

        for i in range(0, len(nums) - 1):
            if nums[i] != nums[i + 1]:
                same = False
                break

        if same:
            return 1

        diff = []
        for i in range(0, len(nums) - 1):
            diff.append(nums[i] - nums[i + 1])

        prev = None
        cnt = 1

        for i in range(0, len(diff)):
            if prev is None:
                if diff[i] != 0:
                    prev = diff[i]
            else:
                if prev < 0:
                    if diff[i] > 0:
                        cnt += 1
                        prev = diff[i]
                elif prev > 0:
                    if diff[i] < 0:
                        cnt += 1
                        prev = diff[i]

        return cnt + 1


s = Solution()
# s.wiggleMaxLength([33, 53, 12, 64, 50, 41, 45, 21, 97, 35])
s.wiggleMaxLength([3, 3, 3, 2, 5])
