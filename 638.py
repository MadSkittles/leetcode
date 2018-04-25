class Solution:
    def shoppingOffers(self, price, special, needs):
        self.price = price
        self.special = special
        self.needs = tuple(needs)
        return self.f(0, (0,) * len(price))

    from functools import lru_cache
    @lru_cache(maxsize=None)
    def f(self, index, cur):
        if index >= len(self.special):
            return sum(price * (self.needs[i] - cur[i]) for i, price in enumerate(self.price))
        res = []
        n = tuple(map(lambda x: sum(x), zip(cur, self.special[index][:-1])))
        if all(n[i] <= self.needs[i] for i in range(len(self.needs))):
            res.append(self.special[index][-1] + self.f(index, n))
        res.append(self.f(index + 1, cur))
        res.append(sum(price * (self.needs[i] - cur[i]) for i, price in enumerate(self.price)))
        return min(res)

    def shoppingOffers1(self, price, special, needs):
        from itertools import product
        for i, p in enumerate(price):
            s = [0] * (len(price) + 1)
            s[i], s[-1] = 1, p
            special.append(s)
        dp = {(0,) * len(price): 0}
        for *offer, p in special:
            if any(offer[i] > n for i, n in enumerate(needs)):
                continue
            for n in product(*[range(offer[i], needs[i] + 1) for i in range(len(needs))]):
                dp[n] = min(dp.get(n, float('inf')), dp.get(tuple(n[i] - offer[i] for i in range(len(n))), float('inf')) + p)
        return dp[tuple(needs)]
