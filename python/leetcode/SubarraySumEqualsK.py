from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        current, res = 0, 0
        for i in range(len(nums)):
            current += nums[i]
            if current == k:
                res += 1
            if current - k in dic:
                res += dic[current - k]
            dic[current] += 1

        return res


s = Solution()
s.subarraySum([1, 1, 1], 2)
s.subarraySum([1], 0)
