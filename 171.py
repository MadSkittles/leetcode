class Solution:
    def titleToNumber(self, s):
        res, base = 0, 26
        for _ in range(len(s) - 1):
            res += base
            base *= 26
        for i, c in enumerate(s[::-1]):
            res += (ord(c) - 65) * (26 ** i)
        return res + 1

if __name__ == '__main__':
    solution=Solution()
    print(solution.titleToNumber('AAA'))
