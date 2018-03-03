class Solution:
    def setZeroes(self, matrix):
        row = len(matrix)
        if not row > 0:
            return
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    if i == j == 0:
                        matrix[0][0] = 'rc'
                    else:
                        if isinstance(matrix[i][0], int):
                            matrix[i][0] = 'r'
                        elif matrix[i][0] is 'c':
                            matrix[i][0] = 'rc'

                        if isinstance(matrix[0][j], int):
                            matrix[0][j] = 'c'
                        elif matrix[0][j] is 'r':
                            matrix[0][j] = 'rc'

        for i in range(row):
            if matrix[i][0] is 'r' or matrix[i][0] is 'rc':
                for j in range(col):
                    if i == 0 and (matrix[i][j] is 'c' or matrix[i][j] is 'rc'):
                        continue
                    matrix[i][j] = 0

        for i in range(col):
            if matrix[0][i] is 'c' or matrix[0][i] is 'rc':
                for j in range(row):
                    matrix[j][i] = 0


if __name__ == '__main__':
    solution = Solution()
    # test_case = [[1, 1, 1], [0, 1, 2]]
    # solution.setZeroes(test_case)
    # print(test_case)
    #
    # test_case = [[0,1]]
    # solution.setZeroes(test_case)
    # print(test_case)

    test_case = [[8,3,6,9,7,8,0,6],[0,3,7,0,0,4,3,8],[5,3,6,7,1,6,2,6],[8,7,2,5,0,6,4,0],[0,2,9,9,3,9,7,3]]
    solution.setZeroes(test_case)
    print(test_case)
