class Solution:
    def reverseBits(self, n):
        res = 0
        for _ in range(32):
            res += n & 1
            res <<= 1
            n >>= 1
        return res >> 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseBits(43261596))
