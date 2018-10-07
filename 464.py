from functools import lru_cache


class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if desiredTotal <= maxChoosableInteger:
            return True
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        self.desiredTotal = desiredTotal
        cadidates = (None,) + (True,) * maxChoosableInteger
        return self.helper(cadidates, 0)

    @lru_cache(None)
    def helper(self, candidates, s):
        candidates = list(candidates)
        if any(s + i >= self.desiredTotal for i in range(1, len(candidates)) if candidates[i]):
            return True
        res = False
        for i in range(1, len(candidates)):
            if candidates[i]:
                candidates[i] = False
                res |= not self.helper(tuple(candidates), s + i)
                candidates[i] = True
            if res:
                break
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.canIWin(5, 50))

