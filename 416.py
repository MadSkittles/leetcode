class Solution:
    def canPartition(self, nums):
        from itertools import accumulate
        nums = sorted(nums)
        s = [*accumulate(nums, lambda x, y: x + y)]
        if s[-1] & 1:
            return False
        dp = [True] + [False] * s[-1]
        for i in range(len(nums)):
            for j in range(s[i], -1, -1):
                if j >= nums[i]:
                    dp[j] = dp[j] or dp[j - nums[i]]
            if s[i] >= s[-1] // 2:
                break
        return dp[s[-1] // 2]

    def canPartition1(self, nums):
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


if __name__ == '__main__':
    solution = Solution()
    print(solution.canPartition(
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]))
