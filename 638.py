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