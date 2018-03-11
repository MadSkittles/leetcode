class Solution:
    def lengthOfLIS(self, nums):
        length = []
        for i in range(len(nums)):
            length.append(max([length[j] + 1 for j in range(i - 1, -1, -1) if nums[i] > nums[j]] + [1]))
        return max(length + [0])


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS([10, 9, 2, 5, 3, 4]))
