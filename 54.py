class Solution:
    def spiralOrder(self, matrix):
        row, col = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
        result = []
        index = 0
        while len(result) < row * col:
            for i in range(index, col - index):
                result.append(matrix[index][i])
            for i in range(index + 1, row - index):
                result.append(matrix[i][col - index - 1])
            if row - index - 1 > index:
                for i in range(col - index - 2, index - 1, -1):
                    result.append(matrix[row - index - 1][i])
            if col - index - 1 > index:
                for i in range(row - index - 2, index, -1):
                    result.append(matrix[i][index])
            index += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.spiralOrder([]))
