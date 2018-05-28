class Solution:
    def judgePoint24(self, nums):
        self.cal = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}
        from itertools import product, permutations, repeat
        for num in permutations(nums):
            for ops in product(*repeat('+-*/', 3)):
                if self.f(num, ops):
                    return True
        return False

    def f(self, nums, ops):
        if len(nums) == 1:
            return abs(nums[0] - 24) < 10e-6

        return any(self.f(nums[:i] + (self.cal[ops[i]](nums[i], nums[i + 1]),) + nums[i + 2:], ops[:i] + ops[i + 1:]) for i in range(len(ops)) if not (ops[i] == '/' and nums[i + 1] == 0))


if __name__ == '__main__':
    solution = Solution()
    print(solution.judgePoint24([1, 2, 1, 2]))
