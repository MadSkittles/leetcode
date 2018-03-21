# 滑动窗口算法
# 窗口右侧不断的扩展，左侧根据条件进行收缩
# 在本题中，我们不必关心要替换哪个具体的字符，我们只要关心当前窗口内的字符，能否在替换n(n<=k)次字符之后能够全部都一样，这就是左侧收缩的条件

class Solution:
    def characterReplacement(self, s, k):
        from collections import Counter
        lo, hi = 0, -1
        c = Counter()
        for hi in range(0, len(s)):
            c.update(s[hi])
            if hi - lo + 1 - c.most_common(1)[0][1] > k:
                c[s[lo]] -= 1
                lo += 1
        return hi - lo + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.characterReplacement('ABAB', 2))
    print(solution.characterReplacement('AABABBA', 1))
    print(solution.characterReplacement('', 0))
