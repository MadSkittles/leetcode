# 若sum(0...i)%k=n，有j>i，sum(0...j)%k=n，则可知sum(i+1...j)是k的倍数。此题中需要j>i+1。

class Solution:
    def checkSubarraySum(self, nums, k):
        seen, s = {0: -1}, 0
        for index, n in enumerate(nums):
            s = ((s + n) % k) if k else (s + n)
            if s in seen and index > seen[s] + 1:
                return True
            elif s not in seen:
                seen[s] = index
        return False
