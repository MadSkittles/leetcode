# 并查集

class Solution:
    def findRedundantConnection(self, edges):
        self.pre = [*range(len(edges) + 1)]
        for start, end in edges:
            s, e = self.find(start), self.find(end)
            if s == e:
                return [start, end]
            else:
                self.pre[s] = e

    def find(self, x):
        r = x
        while r != self.pre[r]:
            r = self.pre[r]
        i = x
        while i != r:
            i, self.pre[i] = self.pre[i], r
        return r