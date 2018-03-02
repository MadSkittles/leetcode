class Solution:
    def fourSum(self, nums, target):
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 3, len(nums)):
                if j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    continue
                start, end = i + 1, j - 1
                while start < end:
                    s = nums[i] + nums[start] + nums[end] + nums[j]
                    if s < target:
                        start += 1
                    elif s > target:
                        end -= 1
                    else:
                        res.append([nums[i], nums[start], nums[end], nums[j]])
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1
                        start += 1
                        end -= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.fourSum([5, 5, 3, 5, 1, -5, 1, -2], 4))
