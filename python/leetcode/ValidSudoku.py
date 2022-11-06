from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        size = 9
        rowSize = 3

        rowSets, colSets, boxSets = [None for _ in range(size)], [None for _ in range(size)], [None for _ in
                                                                                               range(size)]

        def addToSet(i, j, se):

            if board[i][j] == '.':
                return True

            if board[i][j] in se:
                return False

            se.add(board[i][j])

            return True

        def createRowSet(row):
            se = set()
            for i in range(len(board)):
                if not addToSet(row, i, se):
                    return False

            rowSets[row] = se
            return True

        def createColumnSet(col):
            se = set()
            for i in range(len(board)):
                if not addToSet(i, col, se):
                    return False

            colSets[col] = se
            return True

        def createBoxSet(r1, c1, r2, c2, box):
            if boxSets[box]:
                return boxSets[box]

            se = set()
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if not addToSet(i, j, se):
                        return False

            boxSets[box] = se
            return True

        def getBoxIndex(i, j):
            return ((i // rowSize) * rowSize) + (j // rowSize)

        def helper():

            nonlocal rowSets, colSets, boxSets

            for i in range(size):
                for j in range(size):
                    boxIndex = getBoxIndex(i, j)
                    rowSet, colSet, boxSet = rowSets[i], colSets[i], boxSets[boxIndex]

                    if rowSet is None:
                        rowSet = createRowSet(i)

                    if colSet is None:
                        colSet = createColumnSet(j)

                    if boxSet is None:
                        i1, j1, i2, j2 = i, j, i + rowSize - 1, j + rowSize - 1
                        boxSet = createBoxSet(i1, j1, i2, j2, boxIndex)

                    if not (rowSet and colSet and boxSet):
                        return False

            return True

        helper()


s = Solution()
s.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
