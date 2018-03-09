class Solution:
    def searchMatrix(self, matrix, target):
        if not len(matrix) or not len(matrix[0]):
            return False
        x, y = 0, len(matrix[0]) - 1
        while matrix[x][y] != target:
            if target < matrix[x][y]:
                if y > 0:
                    y -= 1
                else:
                    return False
            if target > matrix[x][y]:
                if x < len(matrix) - 1:
                    x += 1
                else:
                    return False
        return True