class Solution:
    def minDistance(self, word1, word2):
        dp = [[float('inf')] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word2) + 1):
            dp[0][i] = i
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for i, c1 in enumerate(word1, 1):
            for j, c2 in enumerate(word2, 1):
                dp[i][j] = dp[i - 1][j - 1] if c1 == c2 else min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance('intention', 'execution'))
