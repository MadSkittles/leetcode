class Solution:
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf')] * amount
        for c in coins:
            for a in range(1, amount + 1):
                if a >= c and dp[a - c] != float('inf'):
                    dp[a] = min(dp[a], dp[a - c] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1

    def coinChange1(self, coins, amount):
        c = [0] + [float('inf')] * amount
        for i in range(len(c)):
            if c[i] == float('inf'):
                c[i] = min([c[i - coin] + 1 for coin in coins if i >= coin and c[i - coin] > -1] + [float('inf')])
        return c[-1] if c[-1] < float('inf') else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange([368, 305, 204, 88, 148, 423, 296, 125, 346], 7163))
