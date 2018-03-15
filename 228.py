class Solution:
    def summaryRanges(self, nums):
        if len(nums) == 1:
            return [str(nums[0])]
        if len(nums) == 0:
            return []
        res = []
        start = nums[0]
        for i in range(1, len(nums) + 1):
            if i >= len(nums) or nums[i] != nums[i - 1] + 1:
                res.append('%d->%d' % (start, nums[i - 1]) if start != nums[i - 1] else str(start))
                start = nums[i] if i < len(nums) else None
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.summaryRanges([0, 1, 2, 4, 5, 7]))
    print(solution.summaryRanges([0, 1, 2, 4, 5, 6]))
    print(solution.summaryRanges([0, 1, 2, 3, 4, 5, 6]))
    print(solution.summaryRanges([-1]))
