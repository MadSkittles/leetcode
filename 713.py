class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        lo, product, res = 0, 1, 0
        for hi in range(len(nums)):
            product *= nums[hi]
            while lo <= hi and product >= k:
                product //= nums[lo]
                lo += 1
            res += hi + 1 - lo
        return res

    def numSubarrayProductLessThanK1(self, nums, k):
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
