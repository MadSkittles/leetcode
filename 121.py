class Solution:
    def maxProfit(self, prices):
        res, min_ = 0, float('inf')
        for p in prices:
            res = max(res, p - min_)
            min_ = min(min_, p)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7,8]))
    print(solution.maxProfit([7, 6, 4, 3, 1]))
