from collections import defaultdict
from typing import List


class KDiffPairs:

    def __init__(self):
        pass

    def findPairs(self, nums: List[int], k: int) -> int:
        dic, res = defaultdict(int), set()
        for num in nums:
            dic[num] += 1
        for num in nums:
            if num + k in dic:
                tu = (num, num + k)
                if num == num + k:
                    if dic[num] > 1:
                        res.add(tu)
                else:
                    res.add(tu)
        return len(res)


if __name__ == "__main__":
    k = KDiffPairs()
    k.findPairs([3, 1, 4, 1, 5], 2)
    k.findPairs([1, 2, 3, 4, 5], 1)
    k.findPairs([1, 3, 1, 5, 4], 0)
    k.findPairs([1, 5, 3, 4, 2], 3)
    k.findPairs([8, 12, 16, 4, 0, 20], 4)
    k.findPairs([6, 2, 9, 3, 9, 6, 7, 7, 6, 4], 3)
