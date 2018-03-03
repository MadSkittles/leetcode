class Solution:
    def grayCode(self, n):
        res = [0, 1]
        if n <= 1:
            return res[:n + 1]
        for i in range(2, n + 1):
            base = 2 ** (i - 1)
            res = [i for i in res] + [(base + i) for i in res[::-1]]
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.grayCode(1))
