import operator
from bisect import bisect_left
from itertools import accumulate
from random import randint


class Solution:
    def __init__(self, w):
        self.s = [0, *accumulate(w, operator.add)]

    def pickIndex(self):
        rand = randint(1, self.s[-1])
        pos = bisect_left(self.s, rand)
        return pos - 1


if __name__ == "__main__":
    solution = Solution([1, 3])
    print(solution.pickIndex())
    print(solution.pickIndex())
    print(solution.pickIndex())
    print(solution.pickIndex())
    print(solution.pickIndex())
