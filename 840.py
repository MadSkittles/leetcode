class Solution:
    def numMagicSquaresInside(self, grid):
        if len(grid) < 3:
            return 0
        self.grid = grid
        res = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid) - 2):
                res += self.check(i, j)
        return res

    def check(self, i, j):
        return sum(self.grid[i + x][j] for x in range(3)) == sum(self.grid[i][j + x] for x in range(3)) \
               == sum(self.grid[i + x][j + x] for x in range(3)) == sum(self.grid[i + 2 - x][j + x] for x in range(3)) == 15 \
               and {self.grid[i + x][j + y] for x in range(3) for y in range(3)} == {*range(1, 10)}


if __name__ == '__main__':
    solution = Solution()
    print(solution.numMagicSquaresInside([[4, 3, 8, 4],
                                          [9, 5, 1, 9],
                                          [2, 7, 6, 2]]))
