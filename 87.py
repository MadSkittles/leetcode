class Solution:
    def isScramble(self, s1, s2):
        return self.f(s1, s2)

    from functools import lru_cache
    @lru_cache(maxsize=None)
    def f(self, s1, s2):
        if len(s1) == 1:
            return s1 == s2
        return any((self.f(s1[:i], s2[:i]) and self.f(s1[i:], s2[i:])) or (self.f(s1[:i], s2[len(s1) - i:]) and self.f(s1[i:], s2[:len(s1) - i])) for i in range(len(s1)))


if __name__ == '__main__':
    solution = Solution()
    print(solution.isScramble("abc", "bca"))
