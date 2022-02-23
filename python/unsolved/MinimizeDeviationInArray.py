import math
from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heapify(nums)
        while True:
            ele = heappop(nums)
            if ele % 2 == 0:
                heappush(nums, ele)
                break
            heappush(nums, ele * 2)

        max_nums = []

        for ele in nums:
            heappush(max_nums, -1 * ele)

        while True:
            ele = heappop(max_nums)
            if ele % 2 != 0:
                heappush(max_nums, ele)
                break
            heappush(max_nums, ele // 2)

        for i in range(len(max_nums)):
            max_nums[i] = max_nums[i] * -1

        min_ele = math.inf
        max_ele = -math.inf

        for ele in max_nums:
            if ele < min_ele:
                min_ele = ele
            if ele > max_ele:
                max_ele = ele

        return abs(max_ele - min_ele)


s = Solution()
s.minimumDeviation([1, 2, 3, 4])
s.minimumDeviation([4, 1, 5, 20, 3])
s.minimumDeviation([2, 10, 8])
s.minimumDeviation([3, 5])
s.minimumDeviation([10, 4, 3])
