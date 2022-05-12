from heapq import heappush, heappop, heapify


class Solution:
    def maximumProduct(self, nums, k):
        MOD = 10 ** 9 + 7
        heapify(nums)
        while k > 0:
            first = heappop(nums)
            first += 1
            k -= 1
            heappush(nums, first)

        res = 1
        for num in nums:
            res = (res * num) % MOD

        return res % MOD


s = Solution()
s.maximumProduct([6, 3, 3, 2], 2)
s.maximumProduct([0, 4], 5)
