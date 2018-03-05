class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0]:
            return 0
        self.cache = {(0, 0): 1}
        self.obstacleGrid = obstacleGrid
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return self.f(m - 1, n - 1)

    def f(self, x, y):
        cache = self.cache.get((x, y))
        if cache:
            return cache

        if self.obstacleGrid[x][y] == 1:
            res = 0
        elif x == 0 and y > 0:
            res = self.f(x, y - 1)
        elif x > 0 and y == 0:
            res = self.f(x - 1, y)
        else:
            res = self.f(x - 1, y) + self.f(x, y - 1)

        if (x, y) not in self.cache:
            self.cache[(x, y)] = res

        return res
