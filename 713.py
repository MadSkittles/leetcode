# 不要每次都去刷新product和hi，否则会TLE

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        res = 0
        product, hi = 1, 0
        for i, num in enumerate(nums):
            hi = max(i, hi)
            while hi < len(nums) and product * nums[hi] < k:
                product *= nums[hi]
                hi += 1
            res += hi - i
            product = product // num if product >= num else 1
        return res
