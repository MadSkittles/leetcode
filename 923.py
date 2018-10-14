from collections import Counter
from functools import lru_cache


class Solution:
    def threeSumMulti(self, A, target):
        self.c = Counter(A)
        l = sorted(self.c.keys())
        res = 0
        for i in range(len(l)):
            lo, hi = i, len(l) - 1
            while 0 <= lo <= hi < len(l):
                if l[i] + l[lo] + l[hi] == target:
                    res = (res + self.cal_sum(l[i], l[lo], l[hi])) % (10 ** 9 + 7)
                    lo += 1
                elif l[i] + l[lo] + l[hi] < target:
                    lo += 1
                else:
                    hi -= 1
        return res

    def cal_sum(self, a, b, c):
        if a == b == c:
            return sum(self.f(i) for i in range(2, self.c[a]))
        if a == b or b == c:
            return self.f(self.c[b]) * (self.c[c] if a == b else self.c[a])
        return self.c[a] * self.c[b] * self.c[c]

    @lru_cache(None)
    def f(self, n):
        return n * (n - 1) // 2


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumMulti([1, 1, 1, 1], 3))
