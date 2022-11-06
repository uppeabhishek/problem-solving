from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        queen = 'Q'
        empty = '.'

        matrix = [['.' for _ in range(n)] for _ in range(n)]

        def valid(i, j):
            for k in range(n):
                if matrix[k][j] == queen:
                    return False

            i1, j1 = i, j

            while j1 > -1:
                if matrix[i1][j1] == queen:
                    return False
                i1 -= 1
                j1 -= 1

            i1, j1 = i, j

            while j1 < n:
                if matrix[i1][j1] == queen:
                    return False
                i1 -= 1
                j1 += 1

            return True

        def helper(row):

            if row == n:
                print("hello")
                return

            for i in range(n):
                if valid(row, i):
                    matrix[row][i] = queen
                    helper(row + 1)
                matrix[row][i] = empty

        helper(0)


s = Solution()
s.solveNQueens(4)
