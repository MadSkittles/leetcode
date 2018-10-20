class Solution:
    def transpose(self, A):
        row_n, col_n = len(A), len(A[0])
        res = [[None] * row_n for _ in range(col_n)]
        for i, row in enumerate(A):
            for j, val in enumerate(row):
                res[j][i] = val
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(solution.transpose([[1, 2, 3], [4, 5, 6]]))

