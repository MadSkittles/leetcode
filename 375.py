class Solution:
    def getMoneyAmount(self, n):
        need = [[0] * (n + 1) for _ in range(n + 1)]
        for lo in range(n, 0, -1):
            for hi in range(lo + 1, n + 1):
                need[lo][hi] = min(x + max(need[lo][x - 1], need[x + 1][hi]) for x in range(lo, hi))
        return need[1][n]

    def getMoneyAmount1(self, n):
        return self.f(1, n)

    from functools import lru_cache
    @lru_cache(maxsize=None)
    def f(self, lo, hi):
        return min(i + max(self.f(lo, i - 1), self.f(i + 1, hi)) for i in range(lo, hi + 1)) if hi > lo else 0


if __name__ == '__main__':
    solutin = Solution()
    print(solutin.getMoneyAmount(6))
