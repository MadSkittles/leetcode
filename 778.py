class Solution:
    def swimInWater(self, grid):
        N = len(grid)
        from queue import PriorityQueue
        q, visited, res = PriorityQueue(), {(0, 0)}, float('-inf')
        q.put((grid[0][0], 0, 0))
        while not q.empty():
            v, x, y = q.get()
            res = max(res, v)
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if i == j == N - 1:
                    return max(res, grid[i][j])
                if 0 <= i < N and 0 <= j < N and (i, j) not in visited:
                    q.put((grid[i][j], i, j))
                    visited.add((i, j))

    def swimInWater1(self, grid):
        def find(x):
            if d[x] != x:
                d[x] = find(d[x])
            return d[x]

        def union(x, y):
            f1, f2 = find(x), find(y)
            if f1 != f2:
                d[f1] = f2

        pos = {}
        N = len(grid)
        for i in range(N):
            for j in range(N):
                pos[grid[i][j]] = [i, j]

        d = [i for i in range(N ** 2)]
        s, e = 0, N ** 2 - 1

        for i in range(1, N ** 2):
            x, y = pos[i]
            for u, v in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if -1 < u < N and -1 < v < N and grid[u][v] <= i:
                    union(x * N + y, u * N + v)
            f1, f2 = find(s), find(e)
            if f1 == f2:
                return i
