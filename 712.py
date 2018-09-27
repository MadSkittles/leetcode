from itertools import accumulate


class Solution:
    def minimumDeleteSum(self, s1, s2):
        s1_ac, s2_ac = [0] + [*accumulate(map(ord, s1))], [0] + [*accumulate(map(ord, s2))]
        dp = [[0 if i > 0 and j > 0 else (j == 0 and s1_ac[i]) or (i == 0 and s2_ac[j]) for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        for i, c1 in enumerate(s1, 1):
            for j, c2 in enumerate(s2, 1):
                if c1 == c2:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(c1), dp[i][j - 1] + ord(c2), dp[i - 1][j - 1] + ord(c1) + ord(c2))
        return dp[-1][-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumDeleteSum("sea", "eat"))
