class Solution:
    def findDuplicates(self, nums):
        res = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return res

    def findDuplicates1(self, nums):
        i, res = 0, []
        while i < len(nums):
            if nums[i] != i + 1 and nums[i] is not None:
                if nums[nums[i] - 1] != nums[i]:
                    x, y = i, nums[i] - 1
                    nums[x], nums[y] = nums[y], nums[x]
                else:
                    res.append(nums[i])
                    nums[i] = None
                    i += 1
            else:
                i += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
