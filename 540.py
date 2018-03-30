class Solution:
    def singleNonDuplicate(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if (mid == 0 and nums[mid + 1] != nums[mid]) or (mid == len(nums) - 1 and nums[mid - 1] != nums[mid]) or nums[mid - 1] != nums[mid] != nums[mid + 1]:
                return nums[mid]
            if (nums[mid] == nums[mid + 1] and mid & 1) or (nums[mid] == nums[mid - 1] and not mid & 1):
                hi = mid - 1
                continue
            if (nums[mid] == nums[mid - 1] and mid & 1) or (nums[mid] == nums[mid + 1] and not mid & 1):
                lo = mid + 1
        return nums[lo]


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNonDuplicate([3, 3, 7, 7, 10, 10, 11]))
