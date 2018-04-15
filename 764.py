class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        mines = {(i, j) for i, j in mines}
        graph = [[(i, j) not in mines for j in range(N)] for i in range(N)]
        res_graph = [[[0, 0, 0, 0] if graph[i][j] else [-1, -1, -1, -1] for j in range(N)] for i in range(N)]
        for i in range(N):
            for j in range(N):
                if graph[i][j]:
                    res_graph[i][j][0] = res_graph[i - 1][j][0] + 1 if i > 0 else 0
                    res_graph[i][j][1] = res_graph[i][j - 1][1] + 1 if j > 0 else 0

        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if graph[i][j]:
                    res_graph[i][j][2] = res_graph[i][j + 1][2] + 1 if j < N - 1 else 0
                    res_graph[i][j][3] = res_graph[i + 1][j][3] + 1 if i < N - 1 else 0
        res = 0
        for i in range(N):
            for j in range(N):
                res = max(res, min(res_graph[i][j]) + 1)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.orderOfLargestPlusSign(5, [[3, 0], [3, 3]]))
    print(solution.orderOfLargestPlusSign(5, [[4, 2]]))
    print(solution.orderOfLargestPlusSign(2, []))
    print(solution.orderOfLargestPlusSign(1, [[0, 0]]))
