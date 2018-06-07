class Solution:
    def singleNumber(self, nums):
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([4, 1, 2, 1, 2]))
