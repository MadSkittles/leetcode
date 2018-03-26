class Solution:
    def totalHammingDistance(self, nums):
        nums = [bin(n)[2:].rjust(32, '0') for n in nums]
        res = 0
        for i in range(32):
            one_num = 0
            for n in nums:
                one_num += n[i] == '1'
            res += one_num * (len(nums) - one_num)
        return res