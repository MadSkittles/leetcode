class Solution:
    def subsets(self, nums):
        self.nums = nums
        self.result = [[]]
        self.n = len(nums)

        for i in range(1, self.n + 1):
            self.f(i, ())

        return self.result

    def f(self, left, comb):
        if left <= 0:
            self.result.append([self.nums[i] for i in comb])
            return

        start = comb[-1] + 1 if len(comb) > 0 else 0
        if self.n - start < left:
            return

        for i in range(start, self.n):
            self.f(left - 1, (*comb, i))

if __name__ == '__main__':
    solution=Solution()
    print(solution.subsets([1,2,3]))