class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        M, N = len(matrix), len(matrix[0])
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dfs(i, j):
            max_ = 0
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ni < M and 0 <= nj < N and matrix[ni][nj] > matrix[i][j]:
                    max_ = max(max_, dfs(ni, nj))
            return 1 + max_

        return max(dfs(i, j) for i in range(M) for j in range(N))


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestIncreasingPath([[1,2]]))
