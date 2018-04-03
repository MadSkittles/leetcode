# 3-Pointer

class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        res = 0
        for i in range(len(nums) - 1, 1, -1):
            lo, hi = 0, i - 1
            while lo < hi:
                if nums[lo] + nums[hi] <= nums[i]:
                    lo += 1
                else:
                    res += hi - lo
                    hi -= 1
        return res