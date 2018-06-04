class Solution:
    def preimageSizeFZF(self, K):
        l, r = 0, 2 ** 63 - 1
        while l < r:
            m = (l + r) // 2
            c, base = 0, 5
            while base <= m:
                c += m // base
                base *= 5
            if c < K:
                l = m + 1
            elif c > K:
                r = m - 1
            else:
                return 5
        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.preimageSizeFZF(10 ** 9))
