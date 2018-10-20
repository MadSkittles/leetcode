class Solution:
    def projectionArea(self, grid):
        N = len(grid)
        row_max, col_max, res = [0] * N, [0] * N, 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v:
                    res += 1
                    row_max[i], col_max[j] = max(row_max[i], v), max(col_max[j], v)
        return res + sum(row_max) + sum(col_max)


if __name__ == "__main__":
    solution = Solution()
    print(solution.projectionArea([[1, 0], [0, 2]]))
    print(solution.projectionArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    print(solution.projectionArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))
