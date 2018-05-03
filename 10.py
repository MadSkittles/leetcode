class Solution:
    def isMatch(self, s, p):
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(s) + 1):
            dp[i][0] = False
        cnt = 0
        for i in range(1, len(p) + 1):
            cnt += 1 if p[i - 1] != '*' else -1
            dp[0][i] = cnt == 0
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = (j >= 2 and dp[i][j - 2]) or (j >= 2 and (s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[i - 1][j])
                else:
                    dp[i][j] = (s[i - 1] == p[j - 1] or p[j - 1] == '.') and dp[i - 1][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch('aa', 'a*'))
