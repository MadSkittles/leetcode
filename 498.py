class Solution:
    def findDiagonalOrder(self, matrix):
        row = len(matrix)
        if not row:
            return []
        col = len(matrix[0])
        res = []
        for i in range(row + col - 1):
            step = 1 if i & 1 else -1
            if row < col:
                for j in [*range(max(i + 1 - col, 0), min(row, i + 1))][::step]:
                    res.append(matrix[j][i - j])
            else:
                for j in [*range(max(i + 1 - row, 0), min(col, i + 1))][::-step]:
                    res.append(matrix[i - j][j])
        return res