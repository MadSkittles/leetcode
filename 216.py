class Solution:
    def combinationSum3(self, k, n):
        self.k = k
        self.n = n
        self.result = []
        self.f(0, ())
        return self.result

    def f(self, sum, nums):
        if len(nums) >= self.k and sum == self.n:
            self.result.append(nums)
            return
        for i in range(nums[-1] + 1 if len(nums) else 1, 10):
            if len(nums) < self.k:
                if sum + i <= self.n:
                    self.f(sum + i, (*nums, i))


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum3(7, 21))
