class Solution:
    def missingNumber(self, nums):
        index, N = 0, len(nums)
        while index < N:
            while nums[index] < N and nums[index] != index:
                x = min(nums[index], N - 1)
                nums[index], nums[x] = nums[x], nums[index]
            index += 1
        for i, v in enumerate(nums):
            if i != v:
                return i
        else:
            return N


if __name__ == '__main__':
    solution = Solution()
    print(solution.missingNumber([ 0]))
    print(solution.missingNumber([9, 6, 4, 2, 3, 5, 8, 0, 1]))
