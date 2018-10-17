from collections import Counter
from math import gcd
from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck):
        if len(deck) < 2:
            return False
        c = Counter(deck)
        X = reduce(lambda x, y: gcd(x, y), c.values())
        return X >= 2 and all(v % X == 0 for v in c.values())


if __name__ == '__main__':
    solution = Solution()
    print(solution.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
    print(solution.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))
    print(solution.hasGroupsSizeX([1]))
    print(solution.hasGroupsSizeX([1, 1]))
    print(solution.hasGroupsSizeX([1, 1, 2, 2, 2, 2]))
    print(solution.hasGroupsSizeX([1, 1, 1, 1, 2, 2, 2, 2, 2, 2]))
