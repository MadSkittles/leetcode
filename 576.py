class Solution:
    def findPaths(self, m, n, N, i, j):
        graph, res = [[0] * n for _ in range(m)], 0
        graph[i][j] = 1
        for _ in range(N):
            cur = graph
            graph = [[0] * n for _ in range(m)]         # 这里是精髓
            for r, row in enumerate(cur):
                for c, val in enumerate(row):
                    if cur[r][c]:
                        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                            if 0 <= nr < m and 0 <= nc < n:
                                graph[nr][nc] += val
                                graph[nr][nc] %= 10 ** 9 + 7
                            else:
                                res += val
                                res %= 10 ** 9 + 7
        return res