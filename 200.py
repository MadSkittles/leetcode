class Solution:
    def numIslands(self, grid):
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
