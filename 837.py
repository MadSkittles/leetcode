class Solution:
    def new21Game(self, N, K, W):
        if K == 0:
            return 1
        Wsum, dp = 1, [1] + [0] * N
        for i in range(1, N + 1):
            dp[i] = Wsum / W
            if i < K:
                Wsum += dp[i]
            if 0 <= i - W < K:
                Wsum -= dp[i - W]
        return sum(dp[K:])


if __name__ == '__main__':
    solution = Solution()
    print(solution.new21Game(N=21, K=17, W=10))
    print(solution.new21Game(9811,
                             8776,
                             1096))
