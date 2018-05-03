class Solution:
    def isMatch(self, s, p):
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(s) + 1):
            dp[i][0] = False
        flag = True
        for i in range(1, len(p) + 1):
            flag = flag and p[i - 1] == '*'
            dp[0][i] = flag
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    dp[i][j] = (s[i - 1] == p[j - 1] or p[j - 1] == '?') and dp[i - 1][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch('aa', 'a'))
    print(solution.isMatch('aa', '*'))
    print(solution.isMatch('cb', '?a'))
    print(solution.isMatch('adceb', '*a*b'))
    print(solution.isMatch('acdcb', 'a*c?b'))
