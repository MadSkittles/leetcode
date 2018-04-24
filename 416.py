class Solution:
    def canPartition(self, nums):
        self.nums = nums
        s = sum(nums)
        return not s & 1 and self.f(0, s // 2)

    from functools import lru_cache
    @lru_cache(maxsize=None)
    def f(self, index, s):
        if s == 0:
            return True
        if s < 0 or index >= len(self.nums):
            return False
        return self.f(index + 1, s - self.nums[index]) or self.f(index + 1, s)
