class Solution:
    def rob(self, nums):
        if len(nums) > 1:
            return max(self.f(nums[1:]), self.f(nums[:-1]))
        else:
            return self.f(nums)

    def f(self, nums):
        pre_sum, cur_sum = 0, 0
        for i in nums:
            pre_sum, cur_sum = cur_sum, max(pre_sum + i, cur_sum)
        return cur_sum
