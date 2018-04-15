class Solution:
    def search(self, nums, target):
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = int((start + end) / 2)
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            if nums[mid] == target:
                return mid
            if nums[end] < target < nums[start]:
                return -1
            if nums[end] > nums[start]:
                if nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[start] < nums[mid]:
                if nums[mid] < target or nums[end] > target:
                    start = mid + 1
                elif nums[start] < target:
                    end = mid - 1
            else:
                if nums[mid] > target or nums[start] < target:
                    end = mid - 1
                elif nums[end] > target:
                    start = mid + 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([1,2,3,4,5], 2))
