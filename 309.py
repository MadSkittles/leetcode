class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        profit = [0]
        for i, p in enumerate(prices[1:], 1):
            profit.append(
                max(profit[-1], (profit[-3] if len(profit) > 2 else 0) + max(0, p - prices[i - 1],
                                                                             p - prices[i - 2] if i == 2 else 0)))
        return profit[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([1, 2, 3, 0, 2]))
    print(solution.maxProfit([2, 4, 1]))
