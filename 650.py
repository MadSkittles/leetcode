class Solution:
    # 100ms
    def minSteps(self, n):
        dp = [0, 0] + [float('inf')] * (n - 1)
        for i in range(1, (n // 2) + 1):
            for j in range(2, (n // i) + 1):
                dp[i * j] = min(dp[i * j], dp[i] + j)
        return dp[-1]

    # 60ms
    def minSteps1(self, n):
        dp = [0] * (n + 1)
        for i in range(1, (n // 2) + 1):
            for j in range(2, (n // i) + 1):
                dp[i * j] = dp[i] + j
        return dp[-1]

    # 40ms
    def minSteps2(self, n):
        def f(n):
            if n == 1:
                return 0
            i = 2
            while n % i:
                i += 1
            return f(n // i) + i

        return f(n)

    # 408ms
    def minSteps3(self, n):
        dp = {1: {}}
        for i in range(1, n):
            for k in dp[i]:
                dp.setdefault(i + k, {})[k] = min(dp.setdefault(i + k, {}).get(k, float('inf')), dp[i][k] + 1)
            dp.setdefault(i + i, {})[i] = min(dp.setdefault(i + i, {}).get(i, float('inf')), min(dp[i].values(), default=0) + 2)
        return min(dp[n].values(), default=0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minSteps1(4))
