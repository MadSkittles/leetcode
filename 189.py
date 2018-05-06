class Solution:
    def rotate(self, nums, k):
        if not nums:
            return nums
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1 - k)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

    def reverse(self, nums, lo, hi):
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1


if __name__ == '__main__':
    solution = Solution()
    l = [1, 2, 3, 4]
    solution.rotate(l, 0)
    print(l)
