class Solution:
    def xorGame(self, nums):
        from functools import reduce
        s = reduce(lambda x, y: x ^ y, nums, 0)
        return s == 0 or not len(nums) & 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.xorGame([1, 1, 2]))
