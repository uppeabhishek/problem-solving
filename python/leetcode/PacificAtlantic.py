from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m, n = len(heights), len(heights[0])

        paths = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def isValid(i, j):
            return not (i < 0 or j < 0 or i == m or j == n)

        def BFSHelper(queue):

            result = set([])

            while len(queue):

                i, j = queue.popleft()

                current = (i, j)

                result.add(current)

                for path in paths:

                    i1, j1 = i + path[0], j + path[1]
                    nxt = (i1, j1)

                    if isValid(i1, j1) and heights[i][j] >= heights[i1][j1] and nxt not in result:
                        queue.append(nxt)

            return result

        def BFS():

            atlantic_queue = deque([])
            pacific_queue = deque([])

            for i in range(m):
                for j in range(n):
                    current = (i, j)
                    if i == 0 or j == 0:
                        atlantic_queue.append(current)

                    if i == m - 1 or j == n - 1:
                        pacific_queue.append(current)

            res1 = BFSHelper(atlantic_queue)
            res2 = BFSHelper(pacific_queue)

            print(res1.intersection(res2))

        return BFS()


s = Solution()
s.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
