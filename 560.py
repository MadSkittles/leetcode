class Solution:
    def subarraySum(self, nums, k):
        from collections import Counter
        seen, s, res = Counter([0]), 0, 0
        for n in nums:
            s += n
            if s - k in seen:
                res += seen[s - k]
            seen[s] += 1
        return res