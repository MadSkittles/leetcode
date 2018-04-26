class Solution:
    def findLength(self, A, B):
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i, a in enumerate(A, 1):
            for j, b in enumerate(B, 1):
                if a == b:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
        return max(map(max, dp))


if __name__ == '__main__':
    solution = Solution()
    print(solution.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
