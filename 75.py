class Solution:
    def sortColors(self, nums):
        cnt = {0: 0, 1: 0, 2: 0}
        for n in nums:
            cnt[n] += 1
        index = 0
        for i in range(3):
            while cnt[i] > 0:
                nums[index] = i
                index += 1
                cnt[i] -= 1


if __name__ == '__main__':
    solution = Solution()
    test_case = [0, 1, 2, 2, 1, 2, 1, 0, 1, 0]
    solution.sortColors(test_case)
    print(test_case)
