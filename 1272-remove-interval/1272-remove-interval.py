from typing import List


class Solution:

    def addToResult(self, i, j, result):
        if i != j:
            result.append([i, j])

    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:

        result = []

        i1, j1 = toBeRemoved

        for i, j in intervals:
            if i >= i1 and j <= j1:
                continue

            if i >= j1 or j <= i1:
                self.addToResult(i, j, result)
                continue

            if i1 >= i and j1 <= j:
                self.addToResult(i, i1, result)
                self.addToResult(j1, j, result)
                continue

            if j >= i1 >= i:
                self.addToResult(i, i1, result)
                continue

            self.addToResult(j1, j, result)

        return result
