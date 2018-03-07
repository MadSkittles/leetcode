class Solution:
    def largestNumber(self, nums):
        from functools import cmp_to_key
        nums = [str(i) for i in nums]
        nums.sort(key=cmp_to_key(lambda x, y: -1 if (x + y < y + x) else 1), reverse=True)
        result = ''.join(nums)
        while len(result) > 1 and result.startswith('0'):
            result = result[1:]
        return result
