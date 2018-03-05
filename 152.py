class Solution(object):
    def maxProduct(self, nums):
        maximum = big = small = nums[0]
        for n in nums[1:]:
            big, small = max(n, n * big, n * small), min(n, n * big, n * small)
            maximum = max(maximum, big)
        return maximum

    def maxSum(self, nums):
        maximum = sum = nums[0]
        for n in nums[1:]:
            sum = max(n, sum + n)
            maximum = max(maximum, sum)
        return maximum
