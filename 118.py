class Solution:
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            res.append([1 if j == 0 or j == i else res[-1][j - 1] + res[-1][j] for j in range(i + 1)])
        return res

if __name__ == '__main__':
    solution=Solution()
    print(solution.generate(5))
