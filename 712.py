# 最小编辑距离的简化变形

class Solution:
    def minimumDeleteSum(self, s1, s2):
        s1, s2 = [*map(ord, s1)], [*map(ord, s2)]
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        s = 0
        for i in range(len(s1)):
            s += s1[i]
            dp[i + 1][0] = s
        s = 0
        for i in range(len(s2)):
            s += s2[i]
            dp[0][i + 1] = s
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1] + s1[i], dp[i + 1][j] + s2[j])
        return dp[-1][-1]
