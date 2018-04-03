class Solution:
    def fractionAddition(self, expression):
        from functools import reduce
        from math import gcd
        fractions, exp = [], ''
        for i, c in enumerate(expression + '+'):
            if c in '+-' and i > 0:
                fractions.append([*map(int, exp.split('/'))])
                exp=''
            exp += c
        denominator = reduce(lambda x, y: x * y, [d[1] for d in fractions], 1)
        res = sum(d[0] * (denominator // d[1]) for d in fractions)
        g = gcd(res, denominator)
        return '/'.join([str(res // g), str(denominator // g)])