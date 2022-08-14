class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows, cols = len(matrix), len(matrix[0])

        i, j = 0, 0

        result = []

        while i < rows and j < cols:

            for k in range(j, cols):
                result.append(matrix[i][k])

            i += 1

            for k in range(i, rows):
                result.append(matrix[k][cols - 1])

            cols -= 1

            if i < rows:
                for k in range(cols - 1, j - 1, - 1):
                    result.append(matrix[rows - 1][k])

                rows -= 1

            if j < cols:
                for k in range(rows - 1, i - 1, -1):
                    result.append(matrix[k][j])

                j += 1

        return result