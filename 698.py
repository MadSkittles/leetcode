class Solution:
    def canPartitionKSubsets(self, nums, k):
        self.sum = sum(nums)
        if sum(nums) % k != 0:
            return False
        self.nums, self.target = sorted(nums, reverse=True), self.sum // k
        self.used = [False] * len(self.nums)
        for _ in range(k):
            self.f(0, 0)
        return all(self.used)

    def f(self, index, sum):
        if sum == self.target:
            return True
        if sum > self.target or index >= len(self.nums):
            return False
        if not self.used[index]:
            self.used[index] = True
            res = self.f(index + 1, sum + self.nums[index])
            if res:
                return True
            self.used[index] = False
        return self.f(index + 1, sum)