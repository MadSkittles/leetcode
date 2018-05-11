class Solution:
    def minCut(self, s):
        dp = [-1]
        for i in range(len(s)):
            dp.append(min([dp[j] + 1 for j in range(i + 1) if s[j:i + 1] == s[j:i + 1][::-1]]))
        return max(dp[-1], 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCut(''))
