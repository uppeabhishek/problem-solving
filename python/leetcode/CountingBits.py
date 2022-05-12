from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        if n == 2:
            return [0, 1, 1]
        if n == 3:
            return [0, 1, 1, 2]

        prev = [1, 2]
        current = []

        result = [0, 1, 1, 2]

        i = 4
        while i <= n:
            for k in range(0, len(prev)):
                if i == n + 1:
                    break
                ele = prev[k] + 0
                current.append(ele)
                result.append(ele)
                i += 1

            for k in range(0, len(prev)):
                if i == n + 1:
                    break
                ele = prev[k] + 1
                current.append(ele)
                result.append(ele)
                i += 1

            prev = current
            current = []

        return result


s = Solution()
s.countBits(17)
