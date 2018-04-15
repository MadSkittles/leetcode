class Solution:
    def deleteAndEarn(self, nums):
        from collections import Counter
        c = Counter(nums)
        nums = sorted(c.keys())
        res = [0]
        for i, n in enumerate(nums):
            if i > 0 and n - nums[i - 1] == 1:
                res.append(max(res[-2] + n * c[n], res[-1]))
            else:
                res.append(res[-1] + n * c[n])
        return res[-1]
