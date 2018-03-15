class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]


if __name__ == '__main__':
    solution = Solution()
    l = [1, 1, 2, 1, 2, 2, 1]
    solution.wiggleSort(l)
    print(l)
