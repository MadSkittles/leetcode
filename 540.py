class Solution:
    def singleNonDuplicate(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if (mid == 0 and nums[mid + 1] != nums[mid]) or (mid == len(nums) - 1 and nums[mid - 1] != nums[mid]) or nums[mid - 1] != nums[mid] != nums[mid + 1]:
                return nums[mid]
            if nums[mid] == nums[mid + (1 if (mid - lo) & 1 else -1)]:
                hi = mid - 1 - (not (mid - lo) & 1)
            else:
                lo = mid + 1 + (not (mid - lo) & 1)
        return nums[lo]


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNonDuplicate([1, 2, 2, 4, 4, 5, 5, 9, 9]))
    print(solution.singleNonDuplicate([1, 1, 2, 2, 4, 4, 5, 5, 9]))
    print(solution.singleNonDuplicate([1, 1, 2, 4, 4, 5, 5, 9, 9]))
