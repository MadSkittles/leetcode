from itertools import accumulate
from functools import lru_cache


class Solution:
    def stoneGame(self, piles):
        self.acc = [0, *accumulate(piles, lambda x, y: x + y)]
        return self.helper(0, len(piles)) > sum(piles) // 2

    @lru_cache(None)
    def helper(self, start, end):
        if start == end:
            return 0
        return self.acc[end] - self.acc[start] - min(self.helper(start + 1, end), self.helper(start, end - 1))


if __name__ == "__main__":
    solution = Solution()
    print(solution.stoneGame([3, 4, 20, 10, 4, 2, 2, 6, 12, 2, 14, 11, 19, 19, 10, 1, 6, 9, 6, 15]))
