class Solution:
    def firstMissingPositive(self, nums):
        index = 0
        while index < len(nums):
            if 1 <= nums[index] <= len(nums) and nums[index] != index + 1 and nums[index] != nums[nums[index] - 1]:
                x = nums[index] - 1
                nums[x], nums[index] = nums[index], nums[x]
            else:
                index += 1
        for i, v in enumerate(nums):
            if v != i + 1:
                return i + 1
        else:
            return len(nums) + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.firstMissingPositive([1, 1]))
    print(solution.firstMissingPositive([3, 4, -1, 1]))
    print(solution.firstMissingPositive([7, 8, 9, 11, 12]))
