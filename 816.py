class Solution:
    def ambiguousCoordinates(self, S):
        from itertools import product
        S, res = S[1:-1], []
        for i in range(1, len(S)):
            s1, s2 = S[:i], S[i:]
            for n1, n2 in product(self.f(s1), self.f(s2)):
                res.append('({}, {})'.format(n1, n2))
        return res

    def f(self, s):
        if len(s) > 1 and all(map(lambda x: x == '0', s)):
            return []
        if s.startswith('0') and s != '0':
            return [s[0] + '.' + s[1:]] if not s[1:].endswith('0') else []
        res = [s]
        for i in range(1, len(s)):
            if not s[i:].endswith('0'):
                res.append(s[:i] + '.' + s[i:])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.ambiguousCoordinates('(0010)'))
