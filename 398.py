class Solution:
    def __init__(self, nums):
        self.m = {}
        for i, v in enumerate(nums):
            self.m.setdefault(v, []).append(i)

    def pick(self, target):
        from random import choice
        return choice(self.m[target])


if __name__ == '__main__':
    solution = Solution([1, 2, 3, 3, 3])
    print(solution.pick(3))
    print(solution.pick(1))
