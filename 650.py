class Solution:
    def minSteps(self, n):
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[j] + (i // j) for j in range(1, i) if not i % j)
        return dp[-1]

    def minSteps1(self, n):
        dp = {1: {}}
        for i in range(1, n):
            for k in dp[i]:
                dp.setdefault(i + k, {})[k] = min(dp.setdefault(i + k, {}).get(k, float('inf')), dp[i][k] + 1)
            dp.setdefault(i + i, {})[i] = min(dp.setdefault(i + i, {}).get(i, float('inf')), min(dp[i].values(), default=0) + 2)
        return min(dp[n].values(), default=0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minSteps(4))
