class Solution:
    def isInterleave(self, s1, s2, s3):
        return self.f(s1, s2, s3)

    from functools import lru_cache
    @lru_cache(maxsize=None)
    def f(self, s1, s2, s3):
        if (s1 == '' and s2 == '') or s3 == '':
            return s1 == s2 == s3 == ''
        return (self.f(s1[1:], s2, s3[1:]) if s1 and s1[0] == s3[0] else False) or (self.f(s1, s2[1:], s3[1:]) if s2 and s2[0] == s3[0] else False)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
    print(solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
