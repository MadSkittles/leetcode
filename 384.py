class Solution:
    def __init__(self, nums):
        self.origin = nums

    def reset(self):
        return self.origin

    def shuffle(self):
        from random import shuffle
        res = self.origin[:]
        shuffle(res)
        return res


if __name__ == '__main__':
    solution = Solution([1, 2, 3, 4, 5, 6])
    print(solution.shuffle())
    print(solution.reset())
    print(solution.shuffle())
