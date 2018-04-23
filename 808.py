class Solution:
    def soupServings(self, N):
        return self.f(N, N, 1) if N <= 5550 else 1

    from functools import lru_cache
    @lru_cache(maxsize=None)
    def f(self, A_left, B_left, p):
        if A_left <= 0:
            return p if B_left > 0 else p * 0.5
        if B_left <= 0:
            return 0
        return sum(self.f(a, b, p * 0.25) for a, b in [(A_left - 100, B_left), (A_left - 75, B_left - 25), (A_left - 50, B_left - 50), (A_left - 25, B_left - 75)])


if __name__ == '__main__':
    solution = Solution()
    print(solution.soupServings(5551))
