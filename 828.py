class Solution:
    def uniqueLetterString(self, S):
        pre, res, pos = 0, 0, {}
        for i, c in enumerate(S):
            if c not in pos:
                pre = 1 + pre + i
            else:
                pre = pre + i - 2 * pos[c][-1] + (-1 if len(pos[c]) == 1 else pos[c][-2])
            res = (res + pre) % (10 ** 9 + 7)
            pos.setdefault(c, []).append(i)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniqueLetterString('ABC'))
    print(solution.uniqueLetterString('ABA'))
