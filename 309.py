# 状态机DP。
# 分为三个状态：购入(即持有股票，可以由冷却状态买入股票进入，或者由购入状态继续保持进入)，出售(刚刚出售股票进入)，冷却(由出售状态进入或者由冷却状态继续保持进入)
# 主要需要分析清楚各个状态之间如何相互转化，难点在于确定初始状态。

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        buy, sell, cooldown = -prices[0], 0, float('-inf')
        for price in prices:
            buy, sell, cooldown = max(cooldown - price, buy), buy + price, max(sell, cooldown)
        return max(sell, cooldown)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([1, 2, 3, 0, 2]))
    print(solution.maxProfit([2, 1, 4]))
