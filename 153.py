class Solution(object):
    def findMin(self, nums):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if (mid == 0 and nums[start] <= nums[end]) or nums[
                mid] < nums[mid - 1]:
                return nums[mid]

            if nums[end] < nums[start] <= nums[mid]:
                start = mid + 1
            elif nums[mid] <= nums[end] < nums[start]:
                end = mid - 1
            elif nums[start] <= nums[end]:
                return nums[start]
        return None