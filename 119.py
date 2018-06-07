class Solution:
    def getRow(self, rowIndex):
        res = []
        for i in range(rowIndex + 1):
            res = [1 if j == 0 or j == i else res[j - 1] + res[j] for j in range(i + 1)]
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.getRow(3))
