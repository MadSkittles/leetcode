class Solution:
    def subsetsWithDup(self, nums):
        self.nums = nums
        self.result = {()}
        self.n = len(nums)

        for i in range(1, self.n + 1):
            self.f(i, ())

        return list(self.result)

    def f(self, left, comb):
        if left <= 0:
            self.result.add(tuple(sorted(self.nums[i] for i in comb)))
            return

        start = comb[-1] + 1 if len(comb) > 0 else 0
        if self.n - start < left:
            return

        for i in range(start, self.n):
            self.f(left - 1, (*comb, i))


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsetsWithDup([4, 4, 4, 1, 4]))
