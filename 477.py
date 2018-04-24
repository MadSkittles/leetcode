class Solution:
    def totalHammingDistance(self, nums):
        res = 0
        for i in range(32):
            one_num = sum((n >> i) & 1 for n in nums)
            res += one_num * (len(nums) - one_num)
        return res



if __name__ == '__main__':
    solution = Solution()
    print(solution.totalHammingDistance([4, 14, 2]))
