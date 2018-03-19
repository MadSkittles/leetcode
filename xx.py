class Solution:
    def rob(self, nums):
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1], (nums[i - 2] if i >= 2 else 0) + nums[i])
        return max(nums + [0])


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([2, 1, 1, 2]))
