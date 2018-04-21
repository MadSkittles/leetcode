class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        self.row, self.col = len(grid), len(grid[0])
        self.m = [[None if grid[i][j] == '0' else (i, j) for j in range(self.col)] for i in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] == '1':
                    root_i, root_j = self.find(i, j)
                    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if 0 <= x < self.row and 0 <= y < self.col and grid[x][y] == '1':
                            root_x, root_y = self.find(x, y)
                            if not (root_x, root_y) == (root_i, root_j):
                                self.m[root_x][root_y] = (root_i, root_j)
        return sum(1 for i in range(self.row) for j in range(self.col) if self.m[i][j] == (i, j))

    def find(self, x, y):
        while self.m[x][y] != (x, y):
            x, y = self.m[x][y]
        return (x, y)

    def numIslands1(self, grid):
        row = len(grid)
        if not row:
            return 0
        col = len(grid[0])
        from queue import Queue
        res, q = 0, Queue()
        s = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res += 1
                    q.put((i, j))
                    grid[i][j] = 'x'
                    while not q.empty():
                        x, y = q.get()
                        s.add((x, y))
                        for delta_x, delta_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if 0 <= x + delta_x < row and 0 <= y + delta_y < col and grid[x + delta_x][
                                y + delta_y] == '1':
                                grid[x + delta_x][y + delta_y] = 'x'
                                q.put((x + delta_x, y + delta_y))
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.numIslands([["1", "0", "1", "1", "1"], ["1", "0", "1", "0", "1"], ["1", "1", "1", "0", "1"]]))
