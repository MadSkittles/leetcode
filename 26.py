class Solution:
    def removeDuplicates(self, nums):
        index = 1
        while index < len(nums):
            if nums[index] == nums[index - 1]:
                del nums[index]
            else:
                index += 1
        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    l = []
    print(solution.removeDuplicates(l))
    print(l)
