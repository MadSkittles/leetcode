class Solution:
    def minDistance(self, word1, word2):
        dp = [[0 if i == 0 and j == 0 else (max(i, j) if i == 0 or j == 0 else 0) for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        for i, c1 in enumerate(word1, 1):
            for j, c2 in enumerate(word2, 1):
                if c1 == c2:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(1 + dp[i - 1][j], 1 + dp[i][j - 1], 2 + dp[i - 1][j - 1])
        return dp[-1][-1]

    def minDistance1(self, word1, word2):
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i, c1 in enumerate(word1, 1):
            for j, c2 in enumerate(word2, 1):
                if c1 == c2:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return len(word1) + len(word2) - 2 * dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance("sea", "ate"))
