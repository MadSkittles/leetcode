class Solution:
    def magicalString(self, n):
        s, index, res = '122', 2, 1
        while len(s) < n:
            s += ('2' if index & 1 else '1') * int(s[index])
            res += 0 if index & 1 else int(s[index])
            index += 1
        res -= s[n:].count('1')
        return res