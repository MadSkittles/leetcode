# 完全背包问题

class Solution(object):
    def change(self, amount, coins):
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(amount - coin + 1):
                dp[i + coin] += dp[i]
        return dp[-1]
