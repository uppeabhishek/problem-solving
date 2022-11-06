from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        paths = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def isValid(i, j):
            return not (i < 0 or j < 0 or i == m or j == n)

        def search_helper(word, i, j, k):

            if board[i][j] != word[k]:
                return False

            if k == len(word) - 1:
                return True

            board[i][j] = "#"

            result = False

            for path in paths:
                i1, j1 = path[0] + i, path[1] + j
                if isValid(i1, j1):
                    result = search_helper(word, i1, j1, k + 1)
                    if result:
                        break

            board[i][j] = word[k]

            return result

        def search():
            result = []
            for word in words:
                shouldBreak = False
                for i in range(m):
                    for j in range(n):
                        if search_helper(word, i, j, 0):
                            result.append(word)
                            shouldBreak = True
                    if shouldBreak:
                        break
            return result

        return search()


s = Solution()
s.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
            ["oath", "pea", "eat", "rain"])
