class Solution:
    def coinChange(self, coins, amount):
        c = [0] + [float('inf')] * amount
        for i in range(len(c)):
            if c[i] == float('inf'):
                c[i] = min([c[i - coin] + 1 for coin in coins if i >= coin and c[i - coin] > -1] + [float('inf')])
        return c[-1] if c[-1] < float('inf') else -1