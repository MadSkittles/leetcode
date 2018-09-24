from itertools import accumulate


class Solution:
    def largestSumOfAverages(self, A, K):
        s = [*accumulate(A, lambda x, y: x + y)]
        dp = [n / i for i, n in enumerate(s, 1)]
        for i in range(1, K):
            dp = [max(dp[k] + (s[j] - s[k]) / (j - k) for k in range(j)) if j >= i else dp[j] for j in range(len(A))]
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.largestSumOfAverages([9, 1, 2, 3, 9], 3))
