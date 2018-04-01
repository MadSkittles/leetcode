class Solution:
    def optimalDivision(self, nums):
        self.nums = nums
        self.res = float('-inf')
        self.exp = ()
        self.f(nums, (0,))
        result, p_index = [], 1
        for index, v in enumerate(nums):
            if p_index < len(self.exp) and index == self.exp[p_index]:
                result.append('(' + str(v))
            else:
                result.append(str(v))
        return '/'.join(result) + ')' * (len(self.exp) - 1)

    def f(self, nums, cur):
        res = self.get_res(cur)
        if res > self.res:
            self.exp = cur
            self.res = res
        for p in range(1, len(nums) - 1):
            self.f(nums[p:], cur + (p + cur[-1],))

    def get_res(self, exp):
        from functools import reduce
        exp = list(exp)
        nums = self.nums[:]
        while exp and len(nums) > 1:
            pos = exp.pop()
            nums[pos:] = [reduce(lambda x, y: x / y, nums[pos:])]
        return nums[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.optimalDivision([100000, 20000, 10000, 5000, 2500, 2000, 1000, 500, 100, 50]))
