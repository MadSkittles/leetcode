class Solution(object):
    def hammingWeight(self, n):
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingWeight(11))
    print(solution.hammingWeight(128))
