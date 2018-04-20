class Solution:
    def largestSumOfAverages(self, A, K):
        from itertools import accumulate
        dp = [[float('-inf')] * (len(A) + 1) for _ in range(K + 1)]
        s = [*accumulate(A, lambda x, y: x + y)]
        dp[1] = [0] + [v / i for i, v in enumerate(s, 1)]
        for i in range(2, K + 1):
            for j in range(i, len(A) + 1):
                dp[i][j] = max(dp[i - 1][k] + (s[j - 1] - s[k - 1]) / (j - k) for k in range(i - 1, j))
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestSumOfAverages([1], 1))
    print(solution.largestSumOfAverages([9, 1, 2, 3, 9], 3))
