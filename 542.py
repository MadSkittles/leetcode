class Solution:
    def updateMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    matrix[i][j] = min(matrix[i - 1][j] + 1 if i > 0 else float('inf'), matrix[i][j - 1] + 1 if j > 0 else float('inf'))
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                if matrix[i][j] != 0:
                    matrix[i][j] = min(matrix[i][j], matrix[i + 1][j] + 1 if i < len(matrix) - 1 else float('inf'), matrix[i][j + 1] + 1 if j < len(matrix[0]) - 1 else float('inf'))
        return matrix