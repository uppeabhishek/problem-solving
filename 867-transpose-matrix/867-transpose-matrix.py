class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(matrix[0])):
            current = []
            for j in range(len(matrix)):
                current.append(matrix[j][i])
            result.append(current)
        return result