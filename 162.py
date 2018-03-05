class Solution(object):
    def findPeakElement(self, nums):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
                return mid
            if (mid > 0 and nums[mid] > nums[mid - 1]) or (mid < len(nums) - 1 and nums[mid] < nums[mid + 1]):
                start = mid + 1
            else:
                end = mid - 1
        return None