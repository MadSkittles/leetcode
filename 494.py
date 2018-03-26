class Solution:
    def findTargetSumWays(self, nums, S):
        self.nums = nums
        return self.f(0, S)

    from functools import lru_cache
    @lru_cache(maxsize=None)
    def f(self, index, sum):
        if index >= len(self.nums):
            return sum == 0
        return self.f(index + 1, sum + self.nums[index]) + self.f(index + 1, sum - self.nums[index])