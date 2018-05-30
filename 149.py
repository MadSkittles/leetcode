class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return '(%d, %d)' % (self.x, self.y)

    @classmethod
    def get_points(cls, l):
        return [cls(x, y) for x, y in l]


class Solution:
    def maxPoints(self, points):
        from collections import defaultdict, Counter
        points = [(p.x, p.y) for p in points]
        cnt = Counter(points)
        points, res, N = sorted(cnt.keys()), 0, len(cnt)
        for p0 in range(N):
            m = defaultdict(lambda: 0)
            for p1 in range(p0 + 1, N):
                m[self.f(points[p0], points[p1])] += cnt[points[p1]]
            res = max(res, max(m.values(), default=0) + cnt[points[p0]])
        return res

    def f(self, p0, p1):
        if p0[0] == p1[0] or p0[1] == p1[1]:
            return (0, 1) if p0[0] == p1[0] else (1, 0)
        import math
        g = math.gcd(p1[0] - p0[0], p1[1] - p0[1])
        return (p1[0] - p0[0]) // g, (p1[1] - p0[1]) // g


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxPoints(Point.get_points([[1, 1], [1, 1], [2, 2], [2, 2]])))
