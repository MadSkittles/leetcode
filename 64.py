class Solution:
    def minPathSum(self, grid):
        self.grid = grid
        self.cache = {}
        row, col = len(grid), len(grid[0])
        return self.f(row - 1, col - 1)

    def f(self, x, y):
        if (x, y) in self.cache:
            return self.cache[(x, y)]

        res = self.grid[x][y]
        if x == 0 and y > 0:
            res += self.f(x, y - 1)
        elif x > 0 and y == 0:
            res += self.f(x - 1, y)
        elif x > 0 and y > 0:
            res += min(self.f(x - 1, y), self.f(x, y - 1))

        if (x, y) not in self.cache:
            self.cache[(x, y)] = res

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.minPathSum([[1, 3, 1],
                               [1, 5, 1],
                               [4, 2, 1]]))
