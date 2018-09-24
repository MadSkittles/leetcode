from bisect import bisect_left
from functools import cmp_to_key


class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])

        def cmp(x, y):
            if x[0] > y[1]:
                return 1
            elif y[0] > x[1]:
                return -1
            else:
                return 0

        wrapper = cmp_to_key(cmp)
        l = []
        for p in map(wrapper, pairs):
            pos = bisect_left(l, p)
            if pos == len(l):
                l.append(p)
            elif p < l[pos] or p.obj[1] < l[pos].obj[1]:
                l[pos] = p
        return len(l)