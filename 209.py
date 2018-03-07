class Solution:
    def minSubArrayLen(self, s, nums):
        sum, start, end = 0, 0, 0
        min_len = len(nums) + 1
        while start <= end < len(nums):
            sum += nums[end]
            if sum >= s:
                min_len = min(min_len, end - start + 1)
                sum -= nums[start]
                start += 1
                sum -= nums[end]
                end -= 1
            end += 1
        return min_len if min_len < len(nums) + 1 else 0