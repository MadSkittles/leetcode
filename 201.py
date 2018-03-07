class Solution:
    def rangeBitwiseAnd(self, m, n):
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i


if __name__ == '__main__':
    solution = Solution()
    print(solution.rangeBitwiseAnd(3, 4))
