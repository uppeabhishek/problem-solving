from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])

        first_letters = []

        paths = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def isValid(i, j):
            return not (i < 0 or j < 0 or i == m or j == n)

        def search_helper(i, j, k):
            if board[i][j] != word[k]:
                return False

            if k == len(word) - 1:
                return True

            board[i][j] = "#"

            result = False

            for path in paths:
                i1, j1 = path[0] + i, path[1] + j
                if isValid(i1, j1):
                    result = search_helper(i1, j1, k + 1)
                    if result:
                        break

            board[i][j] = word[k]

            return result

        def search():
            for letter in first_letters:
                if search_helper(letter[0], letter[1], 0):
                    return True
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    first_letters.append((i, j))

        return search()


s = Solution()
s.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB")
