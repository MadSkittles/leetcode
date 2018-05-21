class Solution:
    def maxCoins(self, nums):
        nums, dp = [1] + nums + [1], [[0] * (len(nums) + 2) for _ in range(len(nums) + 2)]

        def helper(i, j):
            if dp[i][j] or j - i <= 1:
                return dp[i][j]
            dp[i][j] = max(nums[i] * nums[j] * nums[k] + helper(i, k) + helper(k, j) for k in range(i + 1, j))
            return dp[i][j]

        return helper(0, len(nums) - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxCoins([3, 1, 5, 8]))
