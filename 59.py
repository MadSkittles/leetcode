class Solution:
    def generateMatrix(self, n):
        result = [[None for _ in range(n)] for _ in range(n)]
        index = 1
        step = 0
        while index <= n ** 2:
            for i in range(step, n - step):
                result[step][i] = index
                index += 1
            for i in range(step + 1, n - step):
                result[i][n - step - 1] = index
                index += 1
            for i in range(n - step - 2, step - 1, -1):
                result[n - step - 1][i] = index
                index += 1
            for i in range(n - step - 2, step, -1):
                result[i][step] = index
                index += 1
            step += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateMatrix(4))
