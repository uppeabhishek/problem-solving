from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = len(board)

        def valid(i, j, val):
            for k in range(n):
                if board[i][k] == val:
                    return False

                if board[k][j] == val:
                    return False

            return True

        def helper(i, j):

            if i == n:
                return

            if i == n - 1:
                print("hi")

            if board[i][j] == ".":
                for k in range(1, n + 1):
                    val = str(k)
                    if valid(i, j, val):
                        board[i][j] = val
                        if j != n - 1:
                            helper(i, j + 1)
                        else:
                            helper(i + 1, 0)
                board[i][j] = '.'

            else:
                if j != n - 1:
                    helper(i, j + 1)
                else:
                    helper(i + 1, 0)

        helper(0, 0)


s = Solution()
s.solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
