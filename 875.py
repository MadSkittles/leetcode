import math


class Solution:
    def minEatingSpeed(self, piles, H):
        lo, hi = math.ceil(sum(piles) / H), max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(math.ceil(p / mid) for p in piles) > H:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == "__main__":
    solution = Solution()
    print(solution.minEatingSpeed([30, 11, 23, 4, 20], 6))
