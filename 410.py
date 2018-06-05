class Solution:
    def splitArray(self, nums, m):
        N = len(nums)
        if m >= len(nums):
            return max(nums)
        dp = [[float('inf')] * N for _ in range(m + 1)]
        from itertools import accumulate
        s = [*accumulate(nums, lambda x, y: x + y)]
        dp[1] = s
        sum = [[s[j] - s[i] for j in range(N)] for i in range(N)]
        for i in range(2, m + 1):
            for j in range(i - 1, N):
                dp[i][j] = min(max(dp[i - 1][k], sum[k][j]) for k in range(i - 2, j))
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.splitArray([7, 2, 5, 10, 8], 2))
