class Solution:
    def longestPalindromeSubseq(self, s):
        dp = [[1 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = 2 + (0 if i + 1 == j else dp[i + 1][j - 1])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]