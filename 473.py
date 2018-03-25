class Solution:
    def makesquare(self, nums):
        s = sum(nums)
        if not s % 4 == 0:
            return False
        l = s // 4
        from collections import Counter
        self.c = Counter(nums)
        for _ in range(4):
            n = self.f(0, sorted(self.c.elements(), reverse=True), l, ())
            if not n:
                return False
            self.c.subtract(n)
        return True

    def f(self, index, keys, sum, nums):
        if sum == 0:
            return nums
        if sum < 0 or index >= len(keys):
            return None
        return self.f(index + 1, keys, sum - keys[index], (*nums, keys[index])) \
               or self.f(index + 1, keys, sum, nums)
