class Solution:
    def surfaceArea(self, grid):
        N = len(grid)
        res = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v:
                    res += 2 + 4 * v
                    up, down, left, right = min(v, grid[i - 1][j] if i > 0 else 0), min(v, grid[i + 1][j] if i < N - 1 else 0), min(v, grid[i][j - 1] if j > 0 else 0), min(v, grid[i][j + 1] if j < N - 1 else 0)
                    res -= up + down + left + right
        return res
