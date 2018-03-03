class Solution:
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        x, y = 0, col - 1
        while 0 <= x < row and 0 <= y < col:
            cur_n = matrix[x][y]
            if target > cur_n:
                x += 1
            elif target < cur_n:
                y -= 1
            else:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchMatrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 3))
