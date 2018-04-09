# 最小编辑距离的简化变形

class Solution:
    def minimumDeleteSum(self, s1, s2):
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        s = 0
        for i in range(len(s1)):
            s += ord(s1[i])
            dp[i + 1][0] = s
        s = 0
        for i in range(len(s2)):
            s += ord(s2[i])
            dp[0][i + 1] = s
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1] + ord(s1[i]), dp[i + 1][j] + ord(s2[j]), dp[i][j] + ord(s1[i]) + ord(s2[j]))
        return dp[-1][-1]