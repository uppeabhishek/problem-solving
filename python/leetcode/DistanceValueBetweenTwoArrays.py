from typing import List


class Solution:

    def bsearch(self, nums, ele):
        i, j = 0, len(nums) - 1

        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == ele:
                if mid == 0:
                    return mid + 1
                elif mid == len(nums) - 1:
                    return mid - 1
                else:
                    first, second = abs(nums[mid - 1] - ele), abs(nums[mid + 1] - ele)
                    return mid - 1 if first < second else mid + 1
            elif ele < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1

        first, second = abs(nums[i] - ele), abs(nums[j] - ele)

        return i if first < second else j

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        cnt = 0
        for ele in arr1:
            index = self.bsearch(arr2, ele)
            if arr2[index] - ele <= d:
                cnt += 1
        return cnt


s = Solution()
s.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2)
