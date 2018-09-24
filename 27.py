class Solution:
    def removeElement(self, nums, val):
        cnt = 0
        for i, n in enumerate(nums):
            if n == val:
                cnt += 1
            else:
                nums[i - cnt] = n
        return len(nums) - cnt


if __name__ == '__main__':
    solution = Solution()
    l = [0, 1, 2, 2, 3, 0, 4, 2]
    print(solution.removeElement(l, 2))
    print(l)
