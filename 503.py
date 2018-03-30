class Solution:
    def nextGreaterElements(self, nums):
        long_nums = nums * 2
        res = [float('inf')] * len(long_nums)
        for i in range(len(long_nums) - 2, -1, -1):
            j = i + 1
            while j != float('inf') and long_nums[j] <= long_nums[i]:
                j = res[j]
            res[i] = j
        return [long_nums[r] if r != float('inf') else -1 for r in res[:len(nums)]]