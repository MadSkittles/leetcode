class Solution:
    def search(self, nums, target):
        nums = self.removeDuplicates(nums)
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = int((start + end) / 2)
            if nums[start] == target or nums[end] == target or nums[mid] == target:
                return True
            if nums[end] < target < nums[start]:
                return False
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
                continue
            else:
                if nums[mid] > target or nums[start] < target:
                    end = mid - 1
                elif nums[end] > target:
                    start = mid + 1
                continue

        return False

    def removeDuplicates(self, nums):
        res = []
        for v in nums:
            if not res or v != res[-1]:
                res.append(v)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([1, 1, 2, 1], 2))
