class Solution:
    def singleNumber(self, nums):
        one = two = 0
        for n in nums:
            one, two = (~n & one) | (n & ~(one ^ two)), (~n & two) | (n & one)
        return one


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([2, 2, 3, 2]))
