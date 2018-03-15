class Solution:
    def combinationSum4(self, nums, target):
        count = [1]
        for i in range(1, target + 1):
            count.append(sum([count[i - j] for j in nums if i >= j]))
        return count[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum4([2, 3], 4))
