class Solution:
    from functools import lru_cache
    @lru_cache(100)
    def integerReplacement(self, n):
        if n == 1:
            return 0
        if n & 1:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
        else:
            return 1 + self.integerReplacement(n // 2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.integerReplacement(111111111111))
