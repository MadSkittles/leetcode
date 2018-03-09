class Solution:
    def singleNumber(self, nums):
        from functools import reduce
        diff = reduce(lambda x, y: x ^ y, nums)
        diff &= -diff
        res = [0, 0]
        # 求diff最右的为1的位，等同于
        # i=1
        # while diff&1==1:
        #   diff >>= 1
        #   i <<= 1
        for n in nums:
            if diff & n:
                res[0] ^= n
            else:
                res[1] ^= n
        return res