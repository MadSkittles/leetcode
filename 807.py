class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        res, row_max, col_max = 0, [max(row) for row in grid], [max(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]
        for i, row in enumerate(grid):
            for j, h in enumerate(row):
                res += min(row_max[i], col_max[j]) - h
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
