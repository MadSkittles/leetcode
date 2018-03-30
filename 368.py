class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        dp = []
        for i, n in enumerate(nums):
            dp.append(
                max([(*dp[j], n) for j in range(i - 1, -1, -1) if n % nums[j] == 0], key=lambda x: len(x),
                    default=(n,)))
        return max(dp, key=lambda x: len(x), default=[])