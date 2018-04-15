class Solution:
    def pyramidTransition(self, bottom, allowed):
        self.allowed = {}
        for p in allowed:
            self.allowed.setdefault((p[0], p[1]), []).append(p[2])
        return self.f(bottom)

    from functools import lru_cache
    @lru_cache(maxsize=None)
    def f(self, bottom):
        if len(bottom) == 1:
            return True
        p = []
        for i in range(len(bottom) - 1):
            if (bottom[i], bottom[i + 1]) in self.allowed:
                p.append(self.allowed[(bottom[i], bottom[i + 1])])
            else:
                return False
        from itertools import product
        for b in product(*p):
            if self.f(b):
                return True
        return False