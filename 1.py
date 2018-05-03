class Solution(object):
    def twoSum(self, nums, target):
        lo, hi, nums = 0, len(nums) - 1, sorted((v, i) for i, v in enumerate(nums))
        while lo < hi:
            if nums[lo][0] + nums[hi][0] == target:
                return [nums[lo][1], nums[hi][1]]
            if nums[lo][0] + nums[hi][0] < target:
                lo += 1
            else:
                hi -= 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([3,2,4], 6))
