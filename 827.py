class Solution:
    def largestIsland(self, grid):
        from queue import Queue
        graph, index = [[None] * len(grid) for _ in range(len(grid))], 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1 and graph[i][j] is None:
                    q, visited, size = Queue(), {(i, j)}, 1
                    q.put((i, j))
                    while not q.empty():
                        x, y = q.get()
                        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                            if (nx, ny) not in visited and 0 <= nx < len(grid) and 0 <= ny < len(grid) and grid[nx][ny] == 1:
                                q.put((nx, ny))
                                visited.add((nx, ny))
                                size += 1
                    for x, y in visited:
                        graph[x][y] = (index, size)
                    index += 1
        res = float('-inf')
        for i in range(len(grid)):
            for j in range(len(grid)):
                r = 1 if graph[i][j] is None else graph[i][j][1]
                if graph[i][j] is None:
                    visited = set()
                    for nx, ny in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid) and grid[nx][ny] == 1 and graph[nx][ny][0] not in visited:
                            r += graph[nx][ny][1]
                            visited.add(graph[nx][ny][0])
                res = max(res, r)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestIsland([[1, 0], [0, 1]]))
    print(solution.largestIsland([[1, 1], [1, 0]]))
    print(solution.largestIsland([[1, 1], [1, 1]]))
