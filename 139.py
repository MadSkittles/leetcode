class Solution(object):
    def wordBreak(self, s, words):
        dp = [True]
        for i in range(1, len(s) + 1):
            dp.append(any(dp[j] and s[j:i] in words for j in range(i)))
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        ["a", "aa"]))
