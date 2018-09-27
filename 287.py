class Solution:
    def findDuplicate(self, nums):
        start, end = 1, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if sum(map(lambda x: x <= mid, nums)) <= mid:
                start = mid + 1
            else:
                end = mid - 1
        return start
