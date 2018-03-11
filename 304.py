class NumMatrix:

    def __init__(self, matrix):
        for i in range(len(matrix)):
            for j in range(1, len(matrix[i])):
                matrix[i][j] += matrix[i][j - 1]
        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        return sum(self.matrix[j][col2] - (self.matrix[j][col1 - 1] if col1 > 0 else 0) for j in range(row1, row2 + 1))


obj = NumMatrix([
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
])
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))
print(obj.sumRegion(0, 0, 0, 0))
