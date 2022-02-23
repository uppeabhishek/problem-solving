from typing import List


class RemovingMinimumNumberOfMagicBeans:
    def minimumRemoval(self, beans: List[int]) -> int:
        if len(beans) == 1:
            return 0

        beans.sort()

        total = sum(beans)
        res = total
        current = 0

        for i in range(len(beans)):
            current = current + beans[i]
            left = current - beans[i]
            right = (len(beans) - i - 1) * beans[i]
            res = min(res, total - left - right - beans[i])
        return res


r = RemovingMinimumNumberOfMagicBeans()
# r.minimumRemoval([66, 90, 47, 25, 92, 90, 76, 85, 22, 3])
r.minimumRemoval([4, 1, 6, 5])
# r.minimumRemoval([2, 10, 3, 2])
r.minimumRemoval([1, 4, 5, 6, 10])
