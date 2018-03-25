# 中位数

class Solution(object):
    def minMoves2(self, nums):
        midian = sorted(nums)[len(nums) // 2]
        return sum(abs(i - midian) for i in nums)
