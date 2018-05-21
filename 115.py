class Solution:
    def numDistinct(self, s, t):
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        dp[0] = [1] * (len(s) + 1)
        for i, c1 in enumerate(t, 1):
            for j, c2 in enumerate(s, 1):
                if c1 == c2:
                    dp[i][j] += dp[i - 1][j - 1]
                dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numDistinct("rabbbit", "rabbit"))
    print(solution.numDistinct("babgbag", "bag"))
